# Grammatical-analysis

This project is a grammatical analysis micro service module developed for the Prototype tool to support the initial stage of learning to write in the Spanish language.

## Documentation

The grammatical analysis module consists of a Flask API that receives a text and returns the grammatical analysis of the text performed by the nltk library and openai's GPT-4 model. 

The API has a single endpoint that receives a GET request with a JSON body containing the text to be analyzed. The API returns a JSON with the grammatical analysis of the text.

### Testing

For testing purposes, you can run the Flask project on your local machine. There are two ways to do this: on linux or on Windows environment.

#### Linux

To run the project on a Linux environment, you just need to run the ***localTest.sh*** file. This file will install the necessary dependencies and run the Flask project.

```bash
source localTest.sh
```
#### Windows

To run the project on a Windows environment, you just need to run the ***localTest.ps1*** file. This file will install the necessary dependencies and run the Flask project.

```bash
.\localTest.ps1
```

### Deactivating the virtual environment

> [!IMPORTANT]
> The project requires a virtual environment to run. The script will create it, but you have to deactivate it manually.
>
> To deactivate the virtual environment, run the following command:
> ```bash
> deactivate
> ```
> This command works for both Linux and Windows environments.

> [!CAUTION]
> It is important to deactivate the virtual environment after running the project. If you don't do this, the virtual environment will keep running and it will consume your computer's resources.