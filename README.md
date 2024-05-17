# Virtual-DNA semester project for CS-2002 spring-2024

<span style="color:#000000"> BRIDGING GENES AND PIXELS TO UNVEIL GENETIC CONNECTIONS</span>

![alt text](image-2.png)

|      NAME       | Fingerprint | Model Deployment | Facial Features | Skin Tone | Web<br />Development | Height | Eyes | Blood |
| :-------------: | :---------: | :--------------: | :-------------: | :-------: | :------------------: | :----: | :--: | :---: |
|   Omer Jouhar   |     ✅      |        ✅        |       ✅        |           |          ✅          |        |      |       |
| Mubeen Ali shah |             |                  |                 |           |                      |        |  ✅  |       |
| Muhammad Nauman |             |                  |                 |           |                      |   ✅   |      |  ✅   |
|  Ammar Chattha  |             |                  |       ✅        |           |                      |        |      |       |
|     Zainab      |             |                  |       ✅        |           |                      |        |      |       |
|     Munazah     |             |                  |       ✅        |           |                      |        |      |       |
|    Saad Ali     |             |        ✅        |                 |           |          ✅          |        |  ✅  |       |
|  Mawiya Kaleem  |             |                  |                 |    ✅     |                      |        |      |       |
|   Ahad Malik    |             |                  |                 |    ✅     |                      |        |      |       |
|  Asad Mehmood   |             |                  |                 |           |                      |        |  ✅  |       |
|  Hassan Ahmad   |             |                  |                 |           |                      |   ✅   |      |  ✅   |

**DATASET**

**\.** 1200 Dpi\, 512 by 512 necessary image processing applied

**\.** Data augmentation techniques have been applied to enhance positive images through rotation and image mirroring approaches\. Additionally\, for the negative class\, random pairing of fingerprint data points has been implemented\.

**REFRENCES**

**\.** Maiti\, D\.\, Basak\, M\.\, & Das\, D\. \(2023\)\. Quality and Feature Analysis of Parent and Child Fingerprints in West Bengal\, India\. International Journal for Research in Applied Science & Engineering Technology \(IJRASET\)\, 11\(X\)\, 127\.

**\.** Aigbogun Jr\.\, E\. O\.\, Ibeachu\, C\. P\.\, & Lemuel\, A\. M\. \(2019\)\. Fingerprint pattern similarity: a family\-based study using novel classification\. Anatomy\, doi:10\.2399/ana\.19\.065\.

**APPROACH**

**\.** A Siamese neural network has been implemented using constructive loss function with PyTorch\. A convolutional neural network \(CNN\) employed to create the feature vector\.

![](img/Presnetation1.jpg)

**DATASET**

\_\_ \_\_ **KinFaceW** **\-I \, ** **KinFaceW** **\-II **

\_\_ \_\_ **\. ** Introduced by Lu et al\. in Min Xu\, Ximiao Zhang\, Xiuzhuang Zhou

**\. ** KinFaceW\-I dataset contains 533 pairs of facial images of persons with a kin relation\. Four different kin relations are considered in the dataset: father and daughter \(F\-D\) with 134 pairs\, father and son \(F\-S\) with 156 pairs\, mother and daughter \(M\-D\) with 127 pairs\, mother and son \(M\-S\) with 116 pairs\. Each sample is composed of one parent face image and one child face image\.

**\. ** KinFaceW\-II Dataset consists of 1000 pairs of facial images of individuals with a kin relation\. This database also considers four common kin relations: father and daughter \(F\-D\)\, father and son \(F\-S\)\, mother and daughter \(M\-D\)\, mother and son \(M\-S\)\. Different from the KinFaceW\-I database\, the positive pairs in this dataset are taken from the same photo\.

**REFRENCES**

\_\_ \_\_ **\.** M\. Xu\, X\. Zhang and X\. Zhou\, "Confidence\-Calibrated Face and Kinship Verification\," in IEEE Transactions on Information Forensics and Security\, vol\. 19\, pp\. 372\-384\, 2024\, doi: 10\.1109/TIFS\.2023\.3318957\.

**APPROACH**

\_\_ \_\_ In this we addresses the challenge of confidence estimation in face and kinship verification\, crucial for ensuring reliability and trustworthiness in high\-stakes scenarios\. While existing methods primarily focus on accuracy\, neglecting confidence estimation can lead to unreliable predictions\. To tackle this issue\, we propose an effective confidence measure to convert similarity scores into confidence scores for face pairs\. Additionally\, we introduce Angular Scaling Calibration \(ASC\)\, a simple yet powerful technique that enables existing verification models to generate confidence\-calibrated predictions without requiring model modifications\. Furthermore\, we incorporate uncertainty estimation into the calibrated confidence to enhance model reliability in noisy data settings\. Our approach represents a comprehensive solution for confidence\-calibrated face and kinship verification\, as validated through extensive experiments on four benchmark datasets\. The results demonstrate the efficacy of our proposed method\.

![](img/Presnetation2.png)

**DATASET**

** \.** \_\_ \_\_ Galton height dataset

**APPROACH**

** \. ** In the project\, neural network regression was employed to forecast child height using parental height as input\. The accuracy of the predictions was evaluated by comparing the forecasted child height with actual measurements\. Results within a range of ±2 units were considered acceptable\, demonstrating the efficacy of the predictive model\.

![](img/Presnetation3.png)

**DATASET**

\_\_ \_\_ **\.** \_\_ \_\_ Manual insertion of dataset in code

**APPROACH**

**\.** \_\_ \_\_ Here\, we've employed an approach wherein the provided dataset indicates that certain blood group combinations from parents yield specific blood group outputs in their offspring\. Initially\, we'll consider the blood groups of the parents\, and subsequently\, those of their child\. We'll then determine from the dataset whether these blood group combinations align with our anticipated outcomes\.

![](img/Presnetation4.png)

<span style="color:#000000">Skintone</span> <span style="color:#000000"> Recognition</span>

- **DATASET**
- **\.** The dataset used is of 200\,000 and was refrenced from https://mmlab\.ie\.cuhk\.edu\.hk/projects/CelebA\.html
  - Necessary data augmentations were done like alignment of the pictures\, cropping the images in the same sizes and only using \.jpg format of data\.
- **REFRENCES**
- **\.** IEEE Signal Process\. Lett\.\, 24 \(3\) \(2017\) \, Shakir H\.R\.\, George L\.E\.\, Tuama G\.K 2015 \,
- **\.** Multimodal approach to human\-face detection and tracking IEEE Trans\. Ind\. Electron\.\, 55 \(3\) \(2008\)
- **\.** A comparative assessment of pixel\-based skin detection methods GML Comput\. Vis\. Group \(2005\)
- **APPROACH**
- **\.** In the image processing notebook We used the original CelebA dataset\. It extracts face images using the MTCNN face detection pre\-trained model\, combines them\, and prepares the dataset for skin tone classification\.
  - The skin tone classification notebook uses the processed face images to classify them based on three predefined skin tones: Fair/Light\, Medium/Tan\, and Dark/Deep\. The MobileNetV2 model is employed for this classification task\.

Face Detection

MTCNN

<span style="color:#000000">Skintone</span> <span style="color:#000000"> Recognition</span>

![alt text](image-1.png)
