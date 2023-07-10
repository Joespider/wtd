import sys

TheProgram = "wtd"
VersionName = "0.0.6"

GetAllTags = []

Bash = {"file":{"list":{"default":"ls <args> <file>",
			"args":{"default":"",
				"all":"-a",
				"recursive":"-R",
				"info":"-l"
				}
			},
		"read":{"default":"cat <args> <file>",
			"top":"head -n <lines> <file>",
			"bottom":"tail -n <lines> <file>"
			},
		"replace":{"default":"sed <args> \"s/<old>/<new>/g\" <file>",
			"args":{"default":"",
				"save":"-i"
				}
			},
		"goto":"cd <old> <new>",
		"copy":{"default":"cp <args> <old> <new>",
			"args":{"default":"",
				"force":"-f",
				"ask":"-i",
				"recursive":"-R"
				}
			},
		"rename":{"default":"mv <args> <old> <new>",
			"args":{"default":"",
				"force":"-f",
				"ask":"-i"
				}
			},
		"move":{"default":"mv <args> <old> <new>",
			"args":{"default":"",
				"force":"-f",
				"ask":"-i"
				}
			},
		"perm":"chmod <args> <file>",
		"own":"chown <args> <file>",
		"new":{"dir":{"default":"mkdir <args> <dir>",
				"args":{"default":""
					}
				},
			"file":"touch <file>"
			},
		"remove":{"default":"rm <args> <file>",
			"args":{"default":"",
				"force":"-f",
				"recursive":"-r",
				"ask":"-i"
				}
			},
		"delete":{"default":"rm <args> <file>",
			"args":{"default":"",
				"force":"-f",
				"recursive":"-r",
				"ask":"-i"
				}
			},
		"search":{"default":"grep <args> <search> <file>",
			"args":{"default":""
				}
			},
		},
	"path":{"root":"/",
		"home":{"default":"/home",
			"user":"/home/${USER}",
			"root":"/root"},
		"usb":"/media/${USER}/<usb>",
		"temp":"/tmp",
		"here":"pwd"
		},
	"env":{"user":"${USER}",
		"computer":"${HOSTNAME}"
		},
	"screen":{"clean":"clear",
		"show":"echo <show>"
		},
	"system":{"date":"date <args>"
		},
	"function":""
	}


PS = {"file":{"list":{"default":"Get-ChildItem <args> <file>",
			"args":{"default":"-Name",
				"all":"-Hidden",
				"recursive":"-Recurse",
				"info":""
				}
			},
		"read":{"default":"Get-Content <args> <file>",
			"top":"Get-Content -Head <lines> <file>",
			"bottom":"Get-Content -Tail <lines> <file>"
			},
		"replace":{"default":"$(Get-Content <file>).replace(<old>,<new>)",
			"args":{"default":""
				}
			},
		"goto":"Set-Location <dir>",
		"copy":{"default":"Copy-Item <args> -Path <old> -Destination <new>",
			"args":{"default":"",
				"force":"-Force",
				"ask":"-Confirm",
				"recursive":"-Recurse"
				}
			},
		"rename":{"default":"Move-Item <args> -Path <old> -Destination <new>",
			"args":{"default":"",
				"force":"-Force",
				"ask":"-Confirm"
				}
			},
		"move":{"default":"Move-Item <args> -Path <old> -Destination <new>",
			"args":{"default":"",
				"force":"-Force",
				"ask":"-Confirm"
				}
			},
		"perm":"chmod <args> <file>",
		"own":"chown <args> <file>",
		"new":{"dir":"New-Item -ItemType Directory -Name <dir>",
			"file":"New-Item -ItemType File -Name <file>"
			},
		"remove":{"default":"Remove-Item <args> <file>",
			"args":{"default":"",
				"force":"-Force",
				"recursive":"-Recurse",
				"ask":"-Confirm"
				}
			},
		"delete":{"default":"Remove-Item <args> <file>",
			"args":{"default":"",
				"force":"-Force",
				"recursive":"-Recurse",
				"ask":"-Confirm"
				}
			},
		"search":"Select-String"
		},
	"path":{"root":"C:\\",
		"home":{"default":"C:\\Users",
			"user":"C:\\Users\\${USER}",
			"root":"C:\\"
			},
		"usb":"[System.IO.DriveInfo]::GetDrives() | ForEach-Object {if($_.VolumeLabel -eq <usb>) { $_.RootDirectory.Name }}",
		"temp":"C:\\Users\\${USER}\\AppData\\Local\\Temp",
		"here":"(Get-Location).Path"
		},
	"env":{"user":"$env:username",
		"computer":"$env:computername"
		},
	"screen":{"clean":"Clear-Host",
		"show":"Write-Output <show>"
		},
	"system":{"date":"Get-Date"
		},
	"function":""
	}

def Help(BashOrPS="", Tag=""):
	if BashOrPS == "" and Tag == "":
		print("Author: joespider")
		print("Program: \""+TheProgram+"\"")
		print("Version: "+VersionName)
		print("Purpose: Createing commands that can be run on Bash and PowerShell")
		print("Usage: "+TheProgram+" <args>")
		print("\t--bash <tag> <args>")
		print("\t--ps <tag> <args>")
		print("")
		print("Get the list of command tags")
		print("\t"+TheProgram+" --bash <tag> --help")
		print("\t"+TheProgram+" --ps <tag> --help")
		print("")
		print("Get the arguments for a given tag")
		print("\t"+TheProgram+" --bash <tag> --help")
		print("\t"+TheProgram+" --ps <tag> --help")
		print("")
		print("Get the fields to input for a given tag")
		print("\t"+TheProgram+" --bash <tag> --fields")
		print("\t"+TheProgram+" --ps <tag> --fields")
		print("")
		print("example:")
		print("\t"+TheProgram+" --bash file.list")
		print("\tls")
		print("\t"+TheProgram+" --bash file.list --fields")
		print("\tls <args> <file>")
		print("\t"+TheProgram+" --bash file.list args=info file=name.txt")
		print("\tls -l name.txt")
		print("")
		print("\t"+TheProgram+" --bash file.copy --fields")
		print("\tcp <args> <old> <new>")
		print("\t"+TheProgram+" --bash file.copy old=me.txt,new=you/")
		print("\tcp me.txt you/")
		print("")
		print("\t"+TheProgram+" --bash file.list --fields")
		print("\tGet-ChildItem <args> <file>")
		print("\t"+TheProgram+" --ps file.list args=info file=name.txt")
		print("\tGet-ChildItem -Name name.txt")
		print("\t"+TheProgram+" --ps file.list args=all,info file=name.txt")
		print("\tGet-ChildItem -Name -Hidden name.txt")
		print("")
		print("\t"+TheProgram+" --ps file.copy --fields")
		print("\tCopy-Item <args> <old> <new>")
		print("\t"+TheProgram+" --ps file.copy old=me.txt,new=you/")
		print("\tCopy-Item me.txt you/")
	elif BashOrPS != "" and Tag == "":
		for Tag in GetAllTags:
			print(Tag)
	else:
		TheKeys = []
		if BashOrPS == "--bash":
			Data = Bash
		elif BashOrPS == "--ps":
			Data = PS

		if Data != {}:
			if "." in Tag:
				Elements = Tag.split(".")
				for elem in Elements:
					if type(Data) is dict:
						if elem in Data.keys():
							Data = Data[elem]
							TheKeys = Data.keys()
			if "args" in TheKeys:
				Keys = []
				for key in Data["args"].keys():
					if key != "args" and key != "default":
						Keys.append(key)
				print("Tag: "+Tag)
				print("Args: "+str(Keys))
				print("")

def Args():
	TheArgs = sys.argv
	TheArgs.pop(0)
	return TheArgs

def GetAllTags(BashOrPS, Data = {}, TheKey="", LastKey=""):
	AllTags = []
	if Data == {}:
		if BashOrPS == "--bash":
			Data = Bash
		elif BashOrPS == "--ps":
			Data = PS

	if Data != {} and type(Data) is dict:
		for tag in Data.keys():
			if tag != "args" and tag != "default":
				newData = Data[tag]
				if LastKey != "" and LastKey not in TheKey:
					TheKey = LastKey+"."+TheKey
				if TheKey != "":
					AllTags.append(TheKey+"."+tag)
				ExtraTags = GetAllTags(BashOrPS,newData,tag,TheKey)
				for NewTag in ExtraTags:
					AllTags.append(NewTag)
	return AllTags

def GetCommand(BashOrPS,Tag):
	TheCommand = ""
	Data = {}

	if BashOrPS == "--bash":
		Data = Bash
	elif BashOrPS == "--ps":
		Data = PS

	if Data != {}:
		if "." in Tag:
			Elements = Tag.split(".")
			for elem in Elements:
				if type(Data) is dict:
					if elem in Data.keys():
						Data = Data[elem]
		else:
			TheCommand = Data[Tag]

		if type(Data) is dict:
			if "default" in Data.keys():
				TheCommand = Data["default"]
		else:
			TheCommand = Data

	return TheCommand

def CommandArgs(TheCommand,Args):
	TheNewCommand = TheCommand
	if " <args> " in TheNewCommand:
		if "args=" not in Args:
			TheCommand = TheNewCommand.split(" <args> ")
			TheNewCommand = " ".join(TheCommand)
		elif "args=" in Args:
			TheCommand = TheNewCommand.split("<args>")
			NewArgs = Args.split("args=",1)[1]
			if "," in NewArgs:
				NewArgsVals = NewArgs.split(",")
				NewArgs = " ".join(NewArgsVals)
				NewArgs = NewArgs.strip()
			TheNewCommand = NewArgs.join(TheCommand)
	return TheNewCommand

def InsertArgs(TheCommand,ArgVals):
	TheNewCommand = TheCommand

	if "," in ArgVals:
		NewArgsVals = ArgVals.split(",")
		ArgVals = "|".join(NewArgsVals)

	if "=" in ArgVals and "|" not in ArgVals:
		ParseArgs = ArgVals.split("=",1)
		TheKey = "<"+ParseArgs[0]+">"
		TheValue = ParseArgs[1]
		if TheKey in TheNewCommand:
			NewCommand = TheNewCommand.split(TheKey)
			TheNewCommand = TheValue.join(NewCommand)

	elif "=" in ArgVals and "|" in ArgVals:
		MultiArgs = ArgVals.split("|")
		for arg in MultiArgs:
			TheNewCommand = InsertArgs(TheNewCommand,arg)
	return TheNewCommand

def HandleArgs(BashOrPs,TheCommand,TheCommandArgs):
	if "args=" in TheCommandArgs:
		if "," in TheCommandArgs:
			TheCommandArgs = TheCommandArgs.split("args=",1)[1]
			NewArgs = "args="
			TheArgs = TheCommandArgs.split(",")
			for AnArg in TheArgs:
				TheCommandArgs = GetCommand(BashOrPs,TheCommand+".args."+AnArg)
				if NewArgs == "args=":
					NewArgs = NewArgs+TheCommandArgs
				else:
					NewArgs = NewArgs+","+TheCommandArgs
			TheCommandArgs = NewArgs
		else:
			if TheCommandArgs == "args=":
				TheCommandArgs = GetCommand(BashOrPs,TheCommand+".args.")
				TheCommandArgs = "args="+TheCommandArgs
			elif "args=" in TheCommandArgs:
				TheCommandArgs = TheCommandArgs.split("args=",1)[1]
				TheCommandArgs = GetCommand(BashOrPs,TheCommand+".args."+TheCommandArgs)
				TheCommandArgs = "args="+TheCommandArgs
			else:
				TheCommandArgs = GetCommand(BashOrPs,TheCommand+".args="+TheCommandArgs)
	return TheCommandArgs

def Main():
	global GetAllTags
	UserIn = Args()
	NumOfInput = len(UserIn)
	if NumOfInput >= 2:
		BashOrPs = UserIn[0]
		TheCommand = UserIn[1]
		GetAllTags = GetAllTags(BashOrPs)
		if TheCommand in GetAllTags:
			Program = GetCommand(BashOrPs,TheCommand)
			if NumOfInput == 2:
				ProgArgs = "args=default"
				ProgArgs = HandleArgs(BashOrPs,TheCommand,ProgArgs)
				Program = CommandArgs(Program,ProgArgs)
				newProgram = []
				OtherArgs = Program.split(" ")
				for Element in OtherArgs:
					if Element.startswith("<") and Element.endswith(">"):
						Element = ""
					if Element != "":
						newProgram.append(Element)

				Program = " ".join(newProgram)
				Program = Program.strip()
				print(Program)
			elif NumOfInput == 3:
				TheCommandArgs = UserIn[2]
				if TheCommandArgs == "--help":
					Help(BashOrPs,TheCommand)
				elif TheCommandArgs == "--fields":
					print(Program)
				elif "args=" not in TheCommandArgs:
					ProgArgs = "args=default"
					ProgArgs = HandleArgs(BashOrPs,TheCommand,ProgArgs)
					Program = CommandArgs(Program,ProgArgs)
					Program = InsertArgs(Program,TheCommandArgs)
					print(Program)
				else:
					TheCommandArgs = HandleArgs(BashOrPs,TheCommand,TheCommandArgs)
					Program = CommandArgs(Program,TheCommandArgs)
					Program = InsertArgs(Program,TheCommandArgs)
					print(Program)
			elif NumOfInput == 4:
				ProgArgs = UserIn[2]
				TheCommandArgs = UserIn[3]
				ProgArgs = HandleArgs(BashOrPs,TheCommand,ProgArgs)
				Program = CommandArgs(Program,ProgArgs)
				Program = InsertArgs(Program,TheCommandArgs)
				print(Program)
		elif TheCommand == "--tags":
			Help(BashOrPs)
	else:
		Help()

if __name__ == '__main__':
	Main()
