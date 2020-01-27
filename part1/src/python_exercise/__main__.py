"""Modus part 1 exercise module"""

import argparse

def main():
    parser = argparse.ArgumentParser(description="Thank you for asking for help. These tools are used to generate a Django project and convert CloudFormation code from YAML to JSON.")
    args = parser.parse_args()
    print("This is our Django project generator tool set.")

if __name__ == '__main__':
    main()