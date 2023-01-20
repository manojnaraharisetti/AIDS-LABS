specialization=["Software Modelling &DevOps","Internet Of Things","Cloud & EdgeComputing","Graphics,Gaming & UX Design","Cyber Security & BlockchainTechnology",
                "Artificial Intelligence & Intelligence Process Automation","Data Science and BigData Analytics","Computer Communications" ]
certification=["Professional scrum Master","None","Linux Essential(101-160)","UnityDeveloper Advance Certification","ETHERIUM Developer AdvanceCertification",
               "PCAP|CertifiedAssociatePythonProgramming","C100DEV:MongoDB certified DeveloperAssociate","None"]
print("Hi I am student advisor chat Bot.")
print("May I know your name?")
name=input()
print("Thank you", name)
print("I am here to help you explore through the specialisations offered in CSE Department of K L University.")
print("Here are the list of specialisations")
for i in range(0,8):
 print((i),".",specialization[i])
print("Choose any specialisation")
ch=int(input())
print("Your courses are:")
print("   Specialisation choosen:",specialization[ch],"\n","   GlobalCertifications:",certification[ch])
