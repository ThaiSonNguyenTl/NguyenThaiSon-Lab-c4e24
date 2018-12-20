import pyexcel
a_list_of_dictionaries = [
    {
        "name": "Adam",
        "age":28
    },
    {
        "name": "Beatrice",
        "age":29
    },
    {
        "name": "Ceri",
        "age":30
    },
    {
        "name": "Dean",
        "age":26
    }
]
pyexcel.save_as(records=a_list_of_dictionaries, dest_file_name="your_file.xlsx")