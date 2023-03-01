# Assignment

### 1.
The graph can be used to determine which fluorophores can be visualized using a filter setup. Fluorophores typically emit light at a specific wavelength, which can be detected by a filter that transmits light at that wavelength. By examining the transmittance graph, I can determine which wavelengths of light will be transmitted through the filter and detected by the microscope. I will be using an open-source database [**FPbase**](https://www.fpbase.org/) together with the [**Fluorescence SpectraViewer**](https://www.thermofisher.com/order/fluorescence-spectraviewer#!/) from Thermo Fisher Scientific to identify fluorophores.

- **d-RFP618**<br>
Ex λ[560] ; Em λ[618]<br>
*(Ex Lambda stands for excitation maximum ; Em Lambda stands for emission maximum)*<br>
Coming from the organism [*Entacmaea quadricolor*](https://www.fpbase.org/organism/6118/), this specific fluorophore is within the range of the given graph.

- **AdRed**<br>
Ex λ[567] ; Em λ[612]<br>
*(Ex Lambda stands for excitation maximum ; Em Lambda stands for emission maximum)*<br>
Coming from the organism [*Acropora digitifera*](https://www.fpbase.org/organism/70779/), this specific fluorophore is within the range of the given graph.

- **RFP611**<br>
Ex λ[559] ; Em λ[611]<br>
*(Ex Lambda stands for excitation maximum ; Em Lambda stands for emission maximum)*<br>
Coming from the organism [*Entacmaea quadricolor*](https://www.fpbase.org/organism/6118/), this specific fluorophore is within the range of the given graph.


### 4.
According to the medical study *"Morphological Features of Cell Death" by U. Ziegler, and P. Groscurth [Published: 01 JUN 2004 - https://doi.org/10.1152/nips.01519.2004]*

Cell death is discriminated into two main forms: apoptosis and necrosis.

![alt text](https://github.com/daniocionini/Digi.Bio-Technical-Assignment/blob/main/img/Features-of-autophagic-apoptotic-and-necrotic-cell-death-Electron-microscopy-images-of.jpeg)

*a) Normal cell; b) autophagic showing the massive formation of (double-membraned) autophagic vacuoles; c) apoptotic cell showing the typical round shape and chromatin condensation; d) necrotic cell showing increased cell size, rupture of cell membrane and vacuoles formation.*

- **Apoptosis**<br>
In contrast to necrosis, apoptosis is a regulated, energy-dependent form of cell death leading to phagocytosis of cellular remnants by neighbouring cells.<br>
Characteristic morphological features:
  - In the nucleus, chromatin condensation and nuclear fragmentation. The condensation starts peripherally along the nuclear membrane, forming a crescent or ringlike structure. During later stages of apoptosis, the nucleus further condenses, and finally, it breaks up inside a cell with an intact cell membrane, a feature described as karyorrhexis.

![alt text](https://github.com/daniocionini/Digi.Bio-Technical-Assignment/blob/main/img/different_cell_death_stages.jpeg)

- **Necrosis**<br>
Characteristic morphological features:
  - a type of cell death that is not programmed but rather accidental. In contrast to apoptosis, necrosis is a passive form of cell death without the intricate regulatory mechanisms that are characteristic of apoptosis. The causes of necrotic cell death such as heat stress or toxic agents can in many cases also induce apoptotic cell death.<br>
  
The morphology of cells dying by necrosis is fairly diverse. The cell membrane becomes permeable early during the death process. Organelles may dilate, and ribosomes may dissociate from the endoplasmic reticulum. The nucleus disintegrates late, and in some cases, chromatin condensation occurs. However, pyknotic and fragmented nuclei are not common features in necrotic cell death. Small charged molecules that normally do not traverse the cell membrane will then enter the cell.


> From the research article *"OrganoidTracker: Efficient cell tracking using machine learning and manual error correction" by Rutger N. U. Kok, Laetitia Hebert, Guizela Huelsz-Prince, Yvonne J. Goos1, Xuan Zheng, Katarzyna Bozek, Greg J. Stephens, Sander J. Tans, Jeroen S. vanZon [Published: October 22, 2020 - https://doi.org/10.1371/journal.pone.0240802]*<br>

> This study investigates the use of convolutional neural networks (CNNs) to automatically detect and classify dead and live cells in phase contrast microscopy images. The authors trained a CNN model using a dataset of over 10,000 annotated images and tested the model's accuracy and performance on a separate dataset of over 1,000 images. The results showed that the CNN model was able to accurately detect and classify dead and live cells, with an overall accuracy of 95.7% and a sensitivity of 95.8%.<br><br>
This study provides an example of how machine learning and image analysis techniques can be used to automate the identification and characterization of dead cells in medical research and clinical applications. 

<br>

Using a Heuristic approach, to identify dead cells from live cells in machine vision software and data consisting of picture frames of a video in grayscale, I would focus on the following principal characteristics of dead cells:<br>

- **Cell morphology**: Living cells tend to have a regular and uniform morphology, while dead cells can have irregular shapes and sizes due to cell shrinkage or swelling.

- **Cell membrane integrity**: The cell membrane is a critical barrier that separates the cell from its external environment. Dead cells often have damaged or ruptured cell membranes, while living cells maintain their membrane integrity.

- **Metabolic activity**: Living cells typically have higher metabolic activity than dead cells, which can be measured using techniques such as fluorescence microscopy with live cell stains or oxygen consumption assays.

- **Nucleus morphology**: The nucleus of a living cell is usually round and uniform in shape, while the nucleus of a dead cell can be fragmented or have irregular shapes due to the breakdown of chromatin.

- **Cytoplasmic granularity**: Living cells often have a uniform and homogenous cytoplasmic texture, while dead cells can have granular or clumped cytoplasmic regions due to cell death processes such as necrosis or apoptosis.

- **Fluorescence staining**: Fluorescent dyes can be used to label specific components of living or dead cells, such as DNA, actin filaments, or mitochondria, which can be used to identify and differentiate the two populations.

By focusing on these physiological characteristics and using appropriate image processing techniques and machine learning algorithms, it may be possible to differentiate between living and dead cells in grayscale video frames.

----
I have deployed a web application, hosted on **Amazon Web Services** through the use of AWS Elastic Beanstalk, employs the Dash framework to facilitate the visualization and analysis of the distinguishing cellular properties of three distinct cell types.<br>
[**Web Application Link**](http://identificationofcells-env.eba-i8vqxvkm.eu-west-2.elasticbeanstalk.com/)

----

### 5.
Assuming the data follows a Gaussian distribution and the sets of numerical values are independent, I would perform a one-way ANOVA test to compute differences between the set's means.<br><br>

I would then perform a Levine's test on the variances to compute if the variances are equal or unequal and set the alpha value for significance at 0.005, where H0 is *'the variances are equal'* and H1 is *'the variances are unequal'*.<br><br>

If the resulting p-value from Levine's test is smaller than 0.005 then we reject the null hypothesis and assume the variances are unequal, the ANOVA test might not be trustworthy. In this case, Welch's ANOVA test might be more appropriate.<br><br>

F-test would be the most appropriate parametric test to compute differences between the standard deviations.<br><br>

If the data does not follow a Gaussian distribution, I would use non-parametric test methods.

### 6.
```
#import the necessary libraries
import pandas as pd 


#open the .csv file
data = pd.read_csv('./dataset/csv_A.csv', sep=';')


#preview the .csv file
print(data.head())


#compute mean and standard deviation and save to new .csv file
(data
    .filter(regex='test', axis=1) #I excluded 'numerosity' from the statistics as it represents the number of observations in the dataset
    .agg(['mean', 'std'], axis=1)
    .to_csv('./dataset/csv_B.csv', index=False)
)


# assert that the file has been correctly exported to the destination
assert_file = pd.read_csv('./dataset/csv_B.csv')
assert 'mean' and 'std' in assert_file.columns, "The csv file is not correctly saved"
```   

### 8.
According to the publication *["Cell Viability Assays"](https://pubmed.ncbi.nlm.nih.gov/23805433/) by Terry L Riss, PhD, Richard A Moravec, BS, Andrew L Niles, MS, Sarah Duellman, PhD, Hélène A Benink, PhD, Tracy J Worzella, MS, and Lisa Minor. [Published May 1, 2013; Last Update: July 1, 2016.]*

*[...]* an introductory overview of the most commonly used assay methods to estimate the number of viable cells in multi-well plates.

- **Tetrazolium Reduction Assays**<br>
MTT which is positively charged and readily penetrates viable eukaryotic cells
MTS, XTT, and WST-1 which are negatively charged and do not readily penetrate cells

- **Resazurin Reduction Assay Concept**<br>
Resazurin is a cell-permeable redox indicator that can be used to monitor viable cell numbers with protocols similar to those utilizing the tetrazolium compounds.

- **TUNEL Assay**<br>
The assay uses a modified dUTP conjugated to a fluorophore to label the 3’OH end of fragmented DNA that is a hallmark of apoptotic cells.

### 9.
To solve this problem I would calculate the proportion.

a : b = c : d

(27-22) : 12 = (22-15) : x

5°C : 12m = 7°C : x

x = (12m * 7°C) / 5°C = 16.8m

The additional time required to reach 15°C is **16.8 minutes**
