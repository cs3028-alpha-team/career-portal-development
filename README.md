# CS3208 Team Alpha - Skillbridge

Welcome to the GitHub repository for Skillbridge, an automated internship match-making software commissioned to Team Alpha by the university's school of medicine, medical sciences and nutrition.
In this document you will find a broad explanation of what the application does and how to run it on your own machine, if you so wish.
A video demostration of the application in action can be found [here](https://clipchamp.com/watch/ZN3sJKAj60H).

#### Running the Application

In order to run the application you will need to have the following softwares installed and set-up on your computer :

1. MySQL Workbench
2. Python 3.1 or above, Python TkInter
3. An IDE (i.e. Visual Studio Code)

Once the above technologies are configured, you will need to tailor the variables in **config.py** to your computer. An example can be found below 
</br>
![config-example](https://github.com/cs3028-alpha-team/career-portal-development/assets/98479421/21285687-d182-4b52-97d7-18c0e7e55619)

Once your development environment has been configured, travel to the project folder and run the command **python main.py** from your terminal of choice.
The Home window will appear on your screen, where you can toggle a checkbox to display the algorithm outputs to screen and run the following actions :

1. Click the **Run match** button to match the current datasets of students and internships, you will see the outputs written to **matches.csv** in the outputs folder.
2. Click the **Settings** button to access the settings dashboard, where you can toggle the fields you would like to the algorithm to use during the matching process and assign a
   priority score to each criteria selected. Please note that you can assign multiple criteria the same priority, if you so wish

Open the **matches.csv** file, where you will find the matches generated by the algorithm. A match will be displayed with the format *match quality*, *student* -> *internship*.
Here is an example from running the default algorithm
</br>
&nsbc;
![output-example](https://github.com/cs3028-alpha-team/career-portal-development/assets/98479421/0c89fe23-f8ef-4108-9466-c3a38e8a2d71)
</br>
To terminate the application, close the Home window.

#### A note from the Team

We hope that this document has helped you gain a better understanding of the purpose of our product. If you encounter any technical difficulties or would like to know more about any of the components involved feel free to send an email at <m.diprofio.21@abdn.ac.uk> - Team Alpha.
