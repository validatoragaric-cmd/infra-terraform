import os
import sys
import argparse
from infra_terraform import Terraform

def parse_args():
    parser = argparse.ArgumentParser(description='Infra Terraform')
    parser.add_argument('--action', type=str, required=True, choices=['init', 'plan', 'apply', 'destroy'])
    parser.add_argument('--path', type=str, default='./')
    return parser.parse_args()

def main():
    args = parse_args()
    terraform = Terraform(args.path)
    if args.action == 'init':
        terraform.init()
    elif args.action == 'plan':
        terraform.plan()
    elif args.action == 'apply':
        terraform.apply()
    elif args.action == 'destroy':
        terraform.destroy()
    else:
        print("Invalid action")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)