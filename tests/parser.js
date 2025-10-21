const fs = require('fs');
const path = require('path');

class TerraformParser {
  constructor(directory) {
    this.directory = directory;
    this.tfFiles = [];
  }

  readDirectory() {
    fs.readdirSync(this.directory).forEach(file => {
      if (path.extname(file) === '.tf') {
        this.tfFiles.push(path.join(this.directory, file));
      }
    });
  }

  parseTfFiles() {
    const parsedFiles = {};
    this.tfFiles.forEach(file => {
      const fileContent = fs.readFileSync(file, 'utf8');
      const fileLines = fileContent.split('\n');
      const resourceBlocks = [];
      let currentBlock = null;

      fileLines.forEach(line => {
        if (line.trim().startsWith('resource')) {
          currentBlock = {
            type: line.trim().split(' ')[1],
            name: line.trim().split(' ')[2],
            properties: {}
          };
        } else if (line.trim().startsWith('}') && currentBlock) {
          resourceBlocks.push(currentBlock);
          currentBlock = null;
        } else if (currentBlock && line.trim().includes('=')) {
          const [key, value] = line.trim().split('=');
          currentBlock.properties[key.trim()] = value.trim().replace(/"|'/g, '');
        }
      });

      parsedFiles[file] = resourceBlocks;
    });

    return parsedFiles;
  }
}

module.exports = TerraformParser;