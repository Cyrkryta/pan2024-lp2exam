# pan2024-lp2exam
Repository for the PAN 2024 exam task on writing style change detection for the Language Processing 2 course at the University of Copenhagen.
As we could not upload the data to git, all the scripts will not run without throwing errors.
- Siamese_lstm.ipynb contains the code used to create the Siamese Neural Network discussed in the report.
- fine_tuning
  - fine-tuning.ipynb contains the model definitions and training of the finetuned models we compare in the report.
  - param_search.ipynb contains the hyperparameter optimization of the base model.
- annotation
  - The folder contains two files.
  - annotation.py is the python script that makes us able to annotate from the terminal
  - test_annotation.csv is the file that the annnotations is saved too.
  - annotation_f1.ipynb is the script for calculating the F1 scores between predicted labels and original labels
- preprocessing
  - preprocessing.ipynb conatins the code for the described preprocessing procedures and creating the datasets
  - aug.ipynb is used to create the augmented datasets
  - aug_concat.ipynb for concatenated and augmneted
  - concat.ipynb to create the concatenated dataset
  - examine.ipynb to check the data

