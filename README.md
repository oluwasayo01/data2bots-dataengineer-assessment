# JSON Schema Sniffer
To run the program, enter the same directory containing the `main.py` file then enter the command below in the terminal.
```bash
python main.py
```


The result is that each json file in the `data` directory has a corresponding json file generated in the `schema` directory which contains it's schema.

To specify separate directories as the data and schema directories, the program can be run using the command
```bash
python main.py --data-dir [dataset] --schema-dir [output]
```
This way, the program reads json files in the specified directory `dataset`, and stores the results in the `output` directory. If the `output` directory does not exist then the program will automatically create it and save the result json files in it.

# Tests
Tests can be run with the command:
```bash
python test.py
```

