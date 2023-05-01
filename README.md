*It is suggested to run this code on Linux

# SETUP:
  - Install conda
  - Clone the repo and build the environment
  
      ```
      git clone https://github.com/crh1987/MachineLearningGroup03CounterFactuals.git
      cd MachineLearningGroup03CounterFactuals/counterfactual_generative_networks
      conda env create -f environment.yml
      conda activate cgn
      ```
      
  - Download u2net.pth from this link: https://drive.google.com/file/d/1ao1ovG1Qtx4b7EoskHXmi2E9rp5CHLcZ/view. Put the u2net.pth file in the imagenet/weights directory. Make all scripts executable and then run
  
      ```
      ./scripts/download_data.sh
      ./scripts/download_weights.sh
      ```
      
# MNISTS:
To run this model with the chinese_MNIST dataset you will:
  
  - Preprocess data
  - Train the CGN
  - Generate counterfactual datasets
  - Train the shape classifier
    
# Preprocess the Data:
  - Download the data at: https://www.kaggle.com/datasets/fedesoriano/chinese-mnist-digit-recognizer/code
  - Move the 'chineseMNIST.csv' file to the counterfactual_generative_network/ folder
  - Run the data processing script:
    
      ```
      python convert_data.py
      ```
      
  - This will create data.npy and chinese_MNIST_data.npy, leave this in the counterfactual_generative_network/ folder
    
# Train the CGN
The configurations and weights of the original researchers were used for this dataset. To train the CGN with the chinese MNIST, run the following with the desired epochs (suggested 15):
    
    
    python mnists/train_cgn.py --cfg mnists/experiments/cgn_chinese_MNIST/cfg.yaml --epochs []
    
    
Add --help for more options. This command saves weights and samples under mnists/experiments/cgn_chinese_MNIST_YEAR_MONTH_DAY_HOUR_MINUTE_SECOND_tmp, where year, month, etc. are the timestamp you trained the CGN. 
    
# Generate Counterfactual Data
Generate the counterfactuals using the weights you just generated. Replace 'WEIGHT_PATH' below with mnists/experiments/cgn_chinese_MNIST_YEAR_MONTH_DAY_HOUR_MINUTE_SECOND_tmp/weights/ckp.pth, with the correct file name.
    
    
    python mnists/generate_data.py \
    --weight_path WEIGHT_PATH \
    --dataset chinese_MNIST --no_cfs 10 --dataset_size 100000
    
    
# Train the Invariant Classifier

    
    python mnists/generate_data.py --dataset chinese_MNIST
    
    
To train the shape classifier and view classification accuracy, run:
    
    
    python mnists/train_classifier.py --dataset chinese_MNIST_counterfactual --epochs [] --lr [] --gamma []
    
