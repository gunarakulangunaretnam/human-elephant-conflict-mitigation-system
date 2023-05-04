# Human Elephant Conflict Mitigation System

## Repo Structure

```text
.
├── docs                                        # Documents Folder.
│   ├── github-readme-content                     # Contains GitHub Readme Content.
│   └── project-documentations                    # Contains Project-related Documents.
├── research                                    # Contains Research files
│   ├── 0-project-prototypes                      # Contains project prototypes; Ex: Detection scripts | TFLITE models.
│   └── 1-supporting-scripts                      # Contains frame extractor & night image vision converter scripts.
├── source                                      # Contains Source Code (Main Project Folder)
│   ├── 0-resources                               # Contains resources: database, requirements.yml.
│   ├── 1-hecms-monitoring-system                 # Contains Monitoring System Project.
│   └── 1-hecms-management-system                 # Contains Management System Project.
├── test                                        # Contains testing scripts.
│   ├── 0-test-case-for-hecms-monitoring-system   # Contains test caes for monitoring system.
│   └── 1-test-case-for-hecms-management-system   # Contains test caes for management system.
├── LICENCE                                     # Licence File.
└── README.MD                                   # Readme file.
```

## 01 Introduction

The human-elephant conflict is a persistent issue in Sri Lanka, where elephants are integral to the country's natural beauty and tourism industry. Due to this conflict, several lives and properties have been lost in rural areas of the country. The Sri Lankan government has been using electric fences to prevent elephants from entering villages, but it is unreliable.

An Artificial Intelligence-based Human Elephant Conflict Mitigation System has been developed to address the persistent issue of human-elephant conflict in Sri Lanka. The system employs CCTV cameras and wildlife camera traps to detect elephants in video frames and subsequently sends early warning messages to the corresponding village authorities to take appropriate actions. Furthermore, the system implements external methods, such as artificial sounds of buzzing bees and firecrackers, to discourage elephants from entering village areas.

The system is designed to provide efficient results during the day and nighttime, and it includes features like elephant detection, early warning SMS/email, and a management system dashboard. The system also updates the conflict information in the database to be analyzed by the conflicts management team.

The system aims to lead Sri Lankan communities in technology to be more powerful and productive to have beautiful lives for everyone. The ultimate goal of this project is to mitigate human-elephant conflicts and promote a sustainable solution for the issue.

![Introduction Image](docs/github-readme-content/banner.png)

## 02 Technology Stack

### 2.1 Primary Programming Tools

| Programming Tools | Version     | Description                     |
| ----------------- | ----------- | ------------------------------- |
| **Python**        | Ver: 3.8    | Use to build monitoring system. |
| **MySQL**         | Ver: 15.1   | Used as central database.       |
| **Laravel**       | Ver: 10.3.3 | Use to build management system. |

### 2.2 Python Dependencies (Monitoring System)

| Programming Tools   | Version       |
| ------------------- | ------------- |
| **TensorFlow**      | Ver: 2.7.0    |
| **Keras**           | Ver: 2.7.0    |
| **OpenCV**          | Ver: 4.6.0.66 |
| **MySQL Connector** | Ver: 2.2.9    |
| **Pillow**          | Ver: 8.4.0    |
| **Pygame**          | Ver: 2.3.0    |
| **PyShorteners**    | Ver: 1.0.1    |

## 03 System Architecture

This section presents an overview of the system architecture for the Artificial Intelligence-based Human Elephant Conflict Mitigation System. The system architecture comprises various elements, including diagrams, flowcharts, components, UML use-case and class diagrams, ER-Diagrams, etc.

### 3.1 Architecture Diagram

![Architecture Diagram](docs/github-readme-content/architecture-diagram.png)

There is a “Head Office” on the right side of the diagram, which means they will use the Management System, and all the conflict incidents data will be transferred to it and can be analyzed and accessed by the Head Office.

On the left side, there are two zones presented as examples, “Habarana Zone” and “Anuradhapura Zone” (Popular elephant conflict places in Sri Lanka), and each zone has a device admin. That device admin has basic access to the Management System through the Device Admin account. Each zone has a Monitoring System installed on a computing device that processes video frames to check elephant presence. If elephants are detected, it will send an SMS to the corresponding villager and an email to “Head Office,” The incident data will be transmitted to Management System. Those can be accessed by “Head Office” and that device admin.In the middle, the database is shared between Management and Monitoring systems to proceed with the granted operations.

### 3.2 Structure Diagram

![Structure Diagram](docs/github-readme-content/structure-diagram.jpg)

The above structured-based architecture diagram clearly explains how the Human Element Conflict Mitigation System (HECMS) functions structurally. HECMS is divided into two main sub-systems: the Monitoring System and the Management System.

Both systems have a shared database in the middle, and their main functionalities are also clearly mentioned; the monitoring system’s primary functions are Elephant detection, SMS sending, Email Sending, artificial sound playing, and database updating, and the management system’s functions are analyzed data, manage data, and create new devices, etc.

### 3.3 Elephant Detection Process Flowchart

![Elephant Detection Process Flowchart](docs/github-readme-content/flowchart-elephant-detection.png)

This flowchart explains how the elephant model detection functions. First, it gets the video stream as the input source; then, it will be transmitted to the next layer to break the video into frames. A frame will be sent to the preprocessing unit to clean up, and then inverts the frame into a numerical vector. The frame will be thrown to the neural network for processing, and then it outputs the confidence value; if the confidence value is greater than or equal to the threshold value, it is considered a positive prediction, and then the system will play artificial sound, send SMS, email, and update database; otherwise, the system processes each frame one by one in a looping manner.

### 3.4 ER Diagram

![ER Diagram](docs/github-readme-content/er-diagram.png)

The ER (Entity-Relationship) diagram explains the structure of the database system in a graphical way; it is the visual representation of the database functions, attributes, and relationships between tables.

The above diagram clearly defines three main tables: Device, Data, and User Accounts. The Data table contains detection data, the Device table includes the monitoring system’s device data, and the User Account table contains the user account details. This is the shared database utilized by both systems Monitoring and Management systems.

### 3.5 Use Case Diagram

![Use Case Diagram](docs/github-readme-content/use-case-diagram.png)

The Use Case Diagram is a Unified Modeling Language (UML) behavioral diagram that represents the Elephant Conflict Mitigation System's interactions between users (Super Admin and Device Admin). The Use Case Diagram can illustrate the system's different use cases or functionalities and the users who interact with the system.

### 3.6 Workflow Diagram

![Use Case Diagram](docs/github-readme-content/workflow.png)

## 04 Setup

This section covers how to set up the human-elephant conflicts mitigation system; this system consists of two main sub-systems: the monitoring system and the management system. The monitoring system is the video processor component that could be installed on a computing device in the jungle to identify elephants; the management system is an analytics system used by the conflicts management team to analyze the incident data. This section shows how to install the necessary dependencies to set it up successfully.

### 4.1 Setup Monitoring System

This project has been designed to operate on both CPU and GPU environments. Utilizing a Graphics Processing Unit (GPU) with CUDA-Enabled technology will enhance the application's performance, allowing faster processing times.

If a GPU is unavailable on the target computer, the system can still be installed and run on the CPU. However, it is essential to note that processing times may be significantly slower when using a CPU than a GPU.

Even though the target computer has a GPU, it is necessary to install CUDA and CUDDN to enable GPU support for TensorFlow. Otherwise, the GPU cannot be utilized but can be run on the CPU.

#### 4.1.1 Installing CUDA & CUDDN (Optional)

It is highly recommended to skip the CUDA & CUDDN installation if the target computer does not have a GPU, as the system can still operate on the CPU. However, it is essential to note that this may result in slower processing times.

Suppose the target computer has a GPU. But if it is chosen not to install CUDA & CUDDN, it is still possible to skip the installation. However, the system can only utilize the CPU power, even though a hardware-based GPU is available. Therefore, CUDA & CUDDN is similar to drivers that enable GPU support.

It is highly recommended to install CUDA & CUDDN if the target computer has a GPU to enable faster processing. The installation steps of CUDA & CUDDN are provided below.

##### Step 01: Checking suitable CUDA & CUDDN verions for TensorFlow.

Check Here:- [https://www.tensorflow.org/install/source#gpu](https://www.tensorflow.org/install/source#gpu)

![TensorFlow Versions](docs/github-readme-content/tensorflow-version.jpg)

The system uses TensorFlow version 2.7.0. To successfully install TensorFlow (version 2.7.0), it is necessary first to install CUDA (version 8.1), followed by CUDDN (version 11.2), as indicated in the accompanying chart. Other versions of TensorFlow might be supported. However, version 2.7.0 is highly recommended; it was tested and developed with this version.

It is important to note that the the above chart provides clear instructions on the appropriate versions of CUDA and CUDDN to install for compatibility with the selected version of TensorFlow.

Accordingly, the installation process should commence with the installation of CUDA, followed by the installation of CUDDN, to ensure that the TensorFlow installation is successful and fully compatible with the selected versions of these dependencies.

##### Step 02: Installing CUDA (Ver: 8.1)

Download CUDA From Here:- [https://developer.nvidia.com/cuda-toolkit-archive](https://developer.nvidia.com/cuda-toolkit-archive)

![TensorFlow Versions](docs/github-readme-content/cuda-version.jpg)

Download and install the appropriate CUDA version from the official website of NVIDIA. The installation process is simple and can be installed with the GUI.

![TensorFlow Versions](github-readme-content/cuda-install.png)

##### Step 03: Installing CUDDN (Ver: 11.2)

Download CUDDN From Here:- [https://developer.nvidia.com/rdp/cudnn-archive](https://developer.nvidia.com/rdp/cudnn-archive)

![TensorFlow Versions](docs/github-readme-content/cuddn-install.jpg)

Download and install the appropriate CUDDN version from the official website of NVIDIA. This time, the installation process could be more challenging.

01.Download and Extract CUDDN zip.

02.There are 3 following folders in it.

```
- bin
- include
- lib
```

03.Open the CUDA Installation directory (WHERE is the CUDA installed) Ex: (C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2)

![TensorFlow Versions](docs/github-readme-content/cuda-install2.png)

04.Copy all content from "bin", "include", "lib" folders from the extracted CUDDN zip to the installed CUDA directory's bin, include, lib. An example is shown above.

##### Step 04: Add CUDA & CUDDN Path to the environment variable.

After successfully installing CUDA and CUDDN, it is important to add their respective paths to the environment variable on your PC. This will ensure that the system is able to locate and use these dependencies when running TensorFlow applications.

01.Add the following path to the environment variable.

- Bin Path
- Libnvp Path

`C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.2\bin`

`C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.2\libnvvp\`

![TensorFlow Versions](docs/github-readme-content/env-path.jpg)

##### Step 05: Check CUDA & CUDDN installed successfully.

- Open CMD and Type

  ```
    nvidia-smi
  ```

  ![TensorFlow Versions](docs/github-readme-content/check-cuda-install.jpg)

**Note:** If it shows like above, that means CUDA & CUDDN have been installed successfully.

#### 4.1.2 Installing Dependencies

This section shows how to install the dependencies easily using the **Anaconda environment** from the requirements.yml. It makes it easy to manage dependencies and create reproducible environments for the projects.

##### **Step 01: Install Anaconda**

The first step is to install Anaconda on the deployed computer: Anaconda is a free and open-source distribution of the Python programming language and a collection of pre-built packages and tools for data science and machine learning. It includes a package manager called "conda" that simplifies the installation and management of packages and dependencies.

- Official Website: https://www.anaconda.com/

##### **Step 02: Navigate to the requirements.yml file directory**

The requirements.yml file is found under this project folder; it could be in the following directory named "hecms-monitoring-system-requirements.yml". Navigate to that directory in CMD.

```
human-elephant-conflict-mitigation-system/source/0-resources/1-requirements/hecms-monitoring-system-requirements.yml
```

- **The requirements file link:** **[hecms-monitoring-system-requirements.yml](source/0-resources/1-requirements/hecms-monitoring-system-requirements.yml)**

##### **Step 03: Install the requirements**

**To Install:** After the navigation to the above directory in CMD then issue the following command to install it; An example screenshot is shown below.

```
 conda env create -f hecms-monitoring-system-requirements.yml
```

- Example screenshot:

- <img src="docs/github-readme-content/install-anaconda-dependencies.jpg" alt="Install using Anaconda Environment" style="border: 1px solid black;">

**IMPORTANT:** It will take some time to install all the dependencies automatically; after the installation, an environment will be created with the name "tensorflow_gpu" that environment contains all the required libraries; when running the HECMS Monitoring System, **always make sure to activate that environment** which has necessary libraries.

**To activate:** Use the following command.

```
activate tensorflow_gpu
```

**Note:** After the activation, the project can be run on top of that environment.

##### Additional Information

There is some additional information below to learn more about the Anaconda environment.

- To Install Anaconda Environment

```
  conda env create -f environment.yml
```

- To Export Anaconda Environment

```
  conda env export > environment.yml
```

- To Delete Anaconda Environment

```
  conda env remove -n ENV_NAME
```

- To Create an Anaconda Environment

```
  conda create -n ENV_NAME python=3.9
```

#### 4.1.3 Setting up Database

The Monitoring and Management systems use the same database to communicate with each other. Therefore, setting up the database first is essential to make both systems work successfully.

To set the database locally, it is recommended to use the XAMPP control panel; there is a MySQL database engine and PHPMyAdmin with it. The database can be found on the following directory.

```
human-elephant-conflict-mitigation-system/source/0-resources/hecms.sql
```

**IMPORTANT:** Give the database name as **hecms**.

![MySQL Database](docs/github-readme-content/setup-database.jpg)

##### Configuring Database

This step configures the database with the monitoring system; suppose the database is hosted remotely. Letting the monitoring system know the credentials and the host is essential. Open the JSON file in the following directory to provide the database credentials and host information.

```
human-elephant-conflict-mitigation-system/source/1-hecms-monitoring-system/assets/credentials/database-credentials.json
```

![MySQL Database Credentials](docs/github-readme-content/database-configure.jpg)

**IMPORTANT:** If the system hosted locally with XAMPP, leave the credentials as same. During the running time of the HECMS Monitoring System, it sends incident information to this database; if the database is hosted somewhere other than localhost, it is important to edit this file.

#### 4.1.4 Setting up Email Sever

**Note:** The HECMS Monitoring System sends emails to the authorities regarding the incidents, to make this function work properly, it is crucial to set up a Google SMTP Email server. Below, the step-by-step guides on setting up the Google SMTP server are provided.

**Step 01:** Choose or create an Google Email to use as a sender: (Ex: hecms_alert@gmail.com)

**Step 02:** Turn on the 2-Step Verification method to allow the email to send mails programmatically.

- <img src="docs/github-readme-content/turn-on-two-factor.jpg" data-canonical-src="github-readme-content/turn-on-two-factor.jpg"/>

**Note 1:** There are some basic process to turn on the two factor authentication, after turning on, follow the step 3.

**Step 03:** Craete an app password | after creating app password, SMTP server can be setup.

- <img src="docs/github-readme-content/set-app-password.jpg" data-canonical-src="github-readme-content/app-password.jpg"/>

- <img src="docs/github-readme-content/create-app-password.jpg" data-canonical-src="github-readme-content/create-app-password.jpg"/>

- <img src="docs/github-readme-content/app-password.jpg" data-canonical-src="github-readme-content/app-password.jpg"/>

Step 04: Enter the app password and the sender email address in the following JSON file:

```
human-elephant-conflict-mitigation-system/source/1-hecms-monitoring-system/assets/credentials/api-credentials.json
```

<img src="docs/github-readme-content/setup-email-smtp-credentials.jpg" data-canonical-src="github-readme-content/create-app-password.jpg"/>

**Note:** Update the email and password under the "google_smtp_server" node.

### 05 Errors & Issues

**Note:** After installation, if any errors occur similar to **"ModuleNotFoundError: No module named 'tensorflow.python.keras.preprocessing'"**, do the following steps to fix it.

**Step 01:**

```
  pip install tensorflow==2.5.0

```

**Step 02:**

```
  pip install tensorflow==2.7.0

```

### 06 Install Dependencies using Anaconda Environment

**What is Conda environment?:** A conda environment is a directory that contains a specific collection of conda packages that you have installed. Anaconda is a tool for simplifying python package management.

**IMPORTANT NOTE:** If it is difficult to install manually one by one, we can install all the necessary dependencies using the Anaconda tool. This repo contains the environment.yml file which has all the libraries that could be installed by issuing the bellow command.

**File is Here:** **[environment.yml](environment.yml)**

#### Commands

- To Install Anaconda Environment

```
  conda env create -f environment.yml

```

- To Export Anaconda Environment

```
  conda env export > environment.yml

```

### 07 Running the system (Execution)

Now, it's time to run our app. We have installed all of the important frameworks. If you find any issues on installation, it's better to do a Google search.

- Clone the repo

```
  git clone https://github.com/GunarakulanGunaretnam/elephant-detection-system-tensorflow.git

```

**Note** This repo contains 4 different projects related to elephant detection system.

### Project Directory layout

    .
    ├── 0-elephant-detection-only                        - Project 1: Elephant Detection.
    ├── 1-elephant-detection-with-alarm-and-email-alert  - Project 2: Alarm + Email Function.
    ├── 2-elephant-detection-with-tensorflow-lite        - Project 3: TensorFlow Lite Model.
    ├── 3-elephant-detection-custom-trained-model        - Project 4: Custom trained model.
    ├── 4-research-works                                 - Contains research files.
    ├── github-readme-content                            - Readme Content Documents.
    ├── environment.yml                                  - Anaconda environment file.
    ├── LICENCE                                          - LICENCE file.
    ├── README.MD                                        - Readme file.

#### 0-elephant-detection-only

=====================

This folder contains the basic elephant detection system. It does only identifying the elephant in video frame. It has no alarming or email sending features. It only has detection part.

This elephant detection is using the ssd_mobilenet_v2_320x320_coco17_tpu-8 dataset model that was trained with COCO-2017 dataset.

This model has more than 80 objects in it. We programmatically muted other objects and allow this model to predict elephant only.

##### Running

```
 python run.py

```

##### To change video source or webcam.

![TensorFlow Versions](github-readme-content/0-elephant-detection-only-webcam.jpg)

Note:- We can give the path of the video to process. If we want to use it as a real time webcam. We can simply put the index of the camera

Example:-

```
 cap = cv2.VideoCapture(0)

```

Note:- 0 is the first camera, 1 is the second camera and 2,3 and etc.

#### 1-elephant-detection-with-alarm-and-email-alert

=======================================

This folder contains the complete elephant detection system with alarming and email sending feature. It is also using the same approach like 0-elephant-detection-only project. But, It has alarming and email sending features.

##### Running

```
 python run.py

```

##### Configuration of email

![TensorFlow Versions](github-readme-content/1-elephant-detection-with-alarm-and-email-alert-email.jpg)

Note:- Here, we have to give the sender-email, sender-password and receiver-email. The sender email is the email that the system is using, the receiver email is the email where the warning message are sent to.

![TensorFlow Versions](github-readme-content/less.jpg)

Note:- We have to turn on the secure less option on to in sender Gmail. Otherwise, we are unable to send emails.

##### To change video source or webcam.

![TensorFlow Versions](github-readme-content/1-elephant-detection-with-alarm-and-email-alert-webcam.jpg)

Note:- We can give the path of the video to process. If we want to use it as a real time webcam. We can simply put the index of the camera

Example:-

```
 cap = cv2.VideoCapture(0)

```

#### 2-elephant-detection-with-tensorflow-lite

=================================

This project is exactly same as the "1-elephant-detection-with-alarm-and-email-alert", But, It is using the tflite model instead of ssd_mobilenet_v2_320x320_coco17_tpu.

TensorFlow Lite (TFLITE) is enabling the deep learning ability in smaller computing devices such as mobile, embedded, and IoT devices.

```
 python run.py

```

- [More info about TFLITE](https://www.tensorflow.org/lite/guide/python)

#### 3-elephant-detection-custom-trained-model

====================================

This project is using a custom trained model. The previous projects are using the ssd_mobilenet_v2_320x320_coco17_tpu COCO-2017 dataset model that has more than 80 objects in it. But, this model customized with only one object that is elephant. This moldel fasther than other models since it has only on object.

```
 python run.py

```

### Output

![Demo1](github-readme-content/demo1.jpg)

![Demo2](github-readme-content/demo2.jpg)

## Social Media Links

- [Linkedin Profile](https://www.linkedin.com/in/gunarakulangunaretnam/)
- [Facebook Page](https://www.facebook.com/gunarakulangunaretnam)
- [Twitter Profile](https://twitter.com/gunarakulan)
- [Instagram Profile](https://www.instagram.com/gunarakulangunaretnam/)
- [Youtube Channel](https://www.youtube.com/channel/UCMWkED5sabgVZSCKjZuRJXA)
