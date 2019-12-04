# Paranuara Planet API

This is a project to provide Checktoporov government an API to have access to its people data on Paranuara planet. Hivery provided [requirements.md](docs\requirements.md) to guide this project.

## Prerequisites

This project needs below software/components be installed on the server. Those that have not installed by default on the server (according to project requirements), will be explained in the next few sections.

1. OS: Microsoft Windows
2. Python 3.7.3
3. Python virtualenv
4. Other required Python modules; listed in [requirements.txt](requirements.txt)
5. MongoDB
6. Postman

## Set Up Environment

To set up project environment, below steps should be followed:

1. Clone the project repository to your machine. Click [here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) to learn more.

2. Install Python **virtualenv**. Open Command Prompt, navigate to project folder in there and run below command:

   `pip install virtualenv`

   Please note, if you are blocked behind corporate firewall, you may need to run below command instead:

   `pip install virtualenv --trusted-host pypi.prg --trusted-host files.pythonhosted.org`

3. To make sure that this project is going to work smoothly and also does not affect the other projects, it is recommended to set up a virtual environment.

   In the open Command Prompt run below command:

   `virtualenv .\venv -p python.exe`

4. When *virtualenv* installation finished, activate created virtual environment by running below command in the same Command Prompt:

   `venv\Scripts\activate.bat`

5. In the existing Command Prompt window run below command to install all required Python packages:

   `pip install -r requirements.txt` 

6. Configure MongoDB. In the MongoDB shell run below commands:

   ```
   use paranuara
   ```

   ```
   db.createUser({user:"hivery",pwd:"test2019",roles:[{role:"readWrite", db:"paranuara"}]})
   ```

   **Note**: Please note that we use `hivery` as user and `test2019` as password. However, you are free to choose whatever you want. But, apply any changes in the rest of configuration accordingly.

7. Add below variables to the user *Environment Variables* for the database connection string. This helps to avoid passing the credential every time we run the application.

   | Key           | Value                                                        |
   | ------------- | ------------------------------------------------------------ |
   | MongoURI      | mongodb://hivery:test2019@127.0.0.1:27017/?authSource=paranuara&authMechanism=SCRAM-SHA-256 |
   | Mongo_Databse | paranuara                                                    |

   **Note 1**: Note that `127.0.0.1:27017` is related to our local MongoDB instance. If you are using different instance on the cloud or you installed it on different server/port, toy should change this part 

   **Note 2**:  Note that `SCRAM-SHA-256` is related to authentication configuration of our local instance of MongoDB. Please change this if your instance configuration is different. See [here](https://docs.mongodb.com/manual/core/authentication-mechanisms/) for more information. 

8. Install Postman. For more information, click [here](https://www.getpostman.com/downloads/).

## Initialise

In this section, we prepare and process the datasets and initialise our database.

### Vegetables and Fruits

Two new JSON files have prepared by using data from [Vegetables Fruits Grains](http://vegetablesfruitsgrains.com/). thses files are stored in [files](files) folder. to import them, we should run below commands in the server that hosts our MongoDB instance. Open Command Prompt window and run these commands:

```
mongoimport --db paranuara --collection vegetable --authenticationDatabase paranuara --username hivery --password test2019 --drop --file [PROJECT PATH]\files\vegetable.json --jsonArray
```

```
mongoimport --db paranuara --collection fruit --authenticationDatabase paranuara --username hivery --password test2019 --drop --file [PROJECT PATH]\files\fruit.json --jsonArray
```

**Note**: Replace `[PROJECT PATH]` with the real path of project in the commands above.

### People and Companies

Before processing people and companies, we need to make sure that our database settings and [*data*](data.py) module work correctly.

Test our data configuration by running below commands in Windows Command Prompt. 

```
cd [PROJECT PATH]
```

```
venv\Scripts\activate.bat
```

```
python.exe tests\test_data_methods_unittest.py
```

You should see below result:


![unittest](https://github.com/aliie62/paranuara_planet/blob/master/docs/test_data_methods_unittest.png)

To preprocess `people.json` and `companies.json` files  and load them into database, run below code in the project virtual environment.

```
python preprocessing\preprocessing.py
```

If there is any food (vegetable or fruit) that has not been found in the database, you should see below output. You need to run `update_foods.py` in folder [preprocessing](preprocessing) to update fruit/vegetable collection.

![failure](https://github.com/aliie62/paranuara_planet/blob/master/docs/preprocessing_error.png)

If everything goes well, you should see below output:

![success](https://github.com/aliie62/paranuara_planet/blob/master/docs/preprocessing_success.png)

**Note**: People username is extracted from their email address.

## Tests

Test scripts are stored in [tests](tests) folder. They should be ran in the project virtual environment. 

## Usage

In the project virtual environment run:

```
python.exe app.py
```

This will run the *app* on `http://127.0.0.1:5000`.

![app](https://github.com/aliie62/paranuara_planet/blob/master/docs/app.png)

**Endpoints** documentations and their examples are exported as json in [`postman_collection.json`](docs). This file should be imported into Postman. To learn more, click [here]().

## Next Step

User management was not included in this release. I am planning to add it in the next version.

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the *MIT License*. See `LICENSE` for more information.
