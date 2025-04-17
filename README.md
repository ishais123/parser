# AWS Cloudtrail Parser

Parser tool written with Python to parse AWS logs from Cloudtrail data source  

## Requirements

| Name | Version |
|------|-------------|
| <a name="eksctl"></a> [pip3](pip3) | 20.2.4 
| <a name="eksctl"></a> [Python](Python) | 3.6.7

## Usage
```bash
# Install requirements
cd parser
pip3 install -r req.txt

# Run Parser
python3 parser.py -f <log file location>
```

## Rollback Process
If you need to rollback to a previous state after parsing:

1. The parser automatically creates backup files with `.bak` extension before processing
2. To rollback, simply rename the backup file by removing the `.bak` extension
3. Example rollback command:
```bash
mv your_logfile.json.bak your_logfile.json
```
