// types.ts
export type TerraformState = {
  version: number;
  terraformVersion: string;
  serial: number;
  lineage: string;
  outputs: { [key: string]: any };
  resources: Resource[];
};

export type Resource = {
  mode: string;
  type: string;
  name: string;
  provider: string;
  instances: Instance[];
};

export type Instance = {
  indexKey: string;
  schemaVersion: number;
  attributes: { [key: string]: any };
  private: string;
  dependencies: string[];
};

export enum ProviderType {
  AWS = 'aws',
  AZURE = 'azurerm',
  GOOGLE = 'google',
}

export type Provider = {
  name: string;
  type: ProviderType;
  region: string;
  credentials: any;
};

export type InfraConfig = {
  name: string;
  description: string;
  providers: Provider[];
  resources: Resource[];
  outputs: { [key: string]: any };
}