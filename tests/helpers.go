package helpers

import (
	"encoding/json"
	"errors"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"

	"github.com/hashicorp/terraform/helper/schema"
)

func fileExists(filename string) bool {
	info, err := os.Stat(filename)
	if os.IsNotExist(err) {
		return false
	}
	return !info.IsDir()
}

func loadJsonFile(filename string, target interface{}) error {
	if !fileExists(filename) {
		return errors.New(fmt.Sprintf("file %s does not exist", filename))
	}
	data, err := ioutil.ReadFile(filename)
	if err != nil {
		return err
	}
	return json.Unmarshal(data, target)
}

func saveJsonFile(filename string, data interface{}) error {
	jsonData, err := json.MarshalIndent(data, "", "  ")
	if err != nil {
		return err
	}
	return ioutil.WriteFile(filename, jsonData, 0644)
}

func getTerraformWorkingDir() (string, error) {
	cwd, err := os.Getwd()
	if err != nil {
		return "", err
	}
	for {
		if fileExists(filepath.Join(cwd, "terraform.tfstate")) {
			return cwd, nil
		}
		parentDir := filepath.Dir(cwd)
		if parentDir == cwd {
			break
		}
		cwd = parentDir
	}
	return "", errors.New("terraform working directory not found")
}

func getTerraformProvider(d *schema.ResourceData, providerName string) (*schema.Resource, error) {
	provider, ok := d.GetOk(providerName)
	if !ok {
		return nil, errors.New(fmt.Sprintf("provider %s not found", providerName))
	}
	providerMap := provider.(map[string]interface{})
	providerSchema := &schema.Resource{
		Schema: providerMap,
	}
	return providerSchema, nil
}

func logError(err error) {
	if err != nil {
		log.Printf("error: %s\n", err)
	}
}