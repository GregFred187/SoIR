# GENERAL

iStartYear = 750
iCalendar = 0

#for messages
iDuration = 20
iWhite = 0
iRed = 7
iGreen = 8
iBlue = 9
iLightBlue = 10
iYellow = 11
iDarkPink = 12
iLightRed = 20
iPurple = 25
iCyan = 44
iBrown = 55
iOrange = 78
iTan = 90
iLime = 139

# Coordinates of Rhye's catapault (should be in some inaccessible area on the edge of the map)
iCatapultX = 114
iCatapultY = 71

# Coordinates of temporary Unit flipping plot (as above)
iFlipX = 114
iFlipY = 69

# Coordinates of temporary Mercenary creation plot (as above)
iMercX = 114
iMercY = 67

# RFC Plague
iImmunity = 20

# RFC Stability Parameters
iNumStabilityParameters = 13
(iParCities3, iParCitiesE, iParCivics3, iParCivics1, iParCivicsE, iParDiplomacy3, iParDiplomacyE, iParEconomy3,
iParEconomy1, iParEconomyE, iParExpansion3, iParExpansion1, iParExpansionE) = range(iNumStabilityParameters)

# City coordinates for religions, free capitals, name updates
tBaghdad = (50,41)
tJerusalem = (33,35)
tConstantinople = (21,63)
tFustat = (24,31)
tMecca = (41,14)
tMedina = (38,24)
tNajaf = (50,37)
tDwarka = (96,16)
tLahore = (106,38)
tDelhi = (111,33)
tSamarra = (49,45)
tAntioch = (36,50)
tArdabil = (59,54)
tDamascus = (37,43)
tRhodes = (19,49)
tTripoli = (35,46)
tAlexandria = (21,34)
tDongola = (21,11)
tAksum = (37,1)

# The AI will not raze these cities
lAINoRaze = [tConstantinople, tJerusalem, tMecca, tMedina, tNajaf, tDwarka, tAntioch, tFustat, tBaghdad, tTripoli, tAlexandria]

# PLAYERS

iNumPlayers = 31
(iByzantium, iMakuria, iAbbasids, iChauhan, iMalwa, iSamanids, iArmenia, iYemen, iBuyids, iGujarat, iGhaznavids, iFatimids, 
iGeorgia, iSindh, iSeljuks, iRum, iKhwarezm, iAntioch, iCrusaders, iZengids, iGhorids, iOman, iAyyubids, iMamluks, iOttomans, 
iBahmanids, iTimurids, iAkKoyunlu, iSafavids, iPortugal, iMughals) = range(iNumPlayers)

iIndependent = iNumPlayers
iIndependent2 = iNumPlayers+1
iIndependent3 = iNumPlayers+2
iIndependent4 = iNumPlayers+3
iBarbarian = 35
iNumMinorPlayers = 4
iNumTotalPlayers = 35

# CAPITALS

tCapitals = (
	(21, 63), # Constantinople
	(21, 11), # Dongola
	(50, 41), # Baghdad
	(107, 26), # Ajmer
	(108, 17), # Dhar
	(95, 51), # Balkh
	(53, 59), # Dvin
	(49,  6), # Sanaa
	(67, 32), # Shiraz
	(102, 20), # Anhilwara
	(96, 41), # Ghazni
	(24, 31), # Cairo
	(54, 63), # Tbilisi
	(97, 24), # Mansura
	(64, 47), # Rayy
	(28, 54), # Konya
	(80, 65), # Urgench
	(36, 50), # Antioch
	(33, 35), # Jerusalem
	(48, 49), # Mosul
	(98, 45), # Kabul
	(75, 20), # Muscat
	(24, 31), # Cairo #	(37, 43), # Damascus
	(24, 31), # Cairo
	(20, 59), # Brusa
	(111,  7), # Ahsenabad
	(94, 58), # Samarkand
	(42, 55), # Diyarbakir
	(59, 54), # Ardabil
	(106,  3), # Goa
	(112, 29), # Agra
) 

# preferred capital if tCapital is not possible
tBackupCapitals = ( 
	(9, 62), # Salonica
	(-1, -1),
	(49, 45), # Samarra
	(106, 21), # Chittor
	(-1, -1),
	(89, 59), # Bukhara
	(-1, -1),
	(-1, -1),
	(-1, -1),
	(-1, -1),
	(106, 38), # Lahore
	(-1, -1),
	(-1, -1),
	(95, 21), # Thatta
	(-1, -1),
	(33, 57), # Kayseri
	(-1, -1),
	(35, 46), # Tripoli
	(32, 39), # Acre
	(-1, -1),
	(90, 43), # Firuzkuh
	(-1, -1),
	(37, 43), # Damascus
	(25, 35), # Domyat
	(21, 63), # Constantinople
	(-1, -1),
	(85, 44), # Herat
	(55, 54), # Tabriz
	(55, 54), # Tabriz
	(-1, -1),
	(106, 38), # Lahore
) 

tRespawnCapitals = (
	(21, 63), # Constantinople
	(21, 11), # Dongola
	(50, 41), # Baghdad
	(106, 21), # Chittor *****
	(108, 17), # Dhar
	(95, 51), # Balkh
	(35, 53), # Sis *****
	(49,  6), # Sanaa
	(67, 32), # Shiraz
	(102, 20), # Anhilwara
	(96, 41), # Ghazni
	(24, 31), # Cairo
	(54, 63), # Tbilisi
	(97, 24), # Mansura
	(64, 47), # Rayy
	(28, 54), # Konya
	(89, 59), # Bukhara ***** #(68, 63), # Khiva *****
	(36, 50), # Antioch
	(30, 46), # Famagusta *****
	(48, 49), # Mosul
	(111, 33), # Delhi *****
	(75, 20), # Muscat
	(37, 43), # Damascus
	(24, 31), # Cairo
	(20, 59), # Brusa
	(11,  7), # Ahsenabad
	(89, 59), # Bukhara
	(42, 55), # Diyarbakir
	(64, 39), # Esfahan
	(106, 3), # Goa
	(112, 29), # Agra
) 

# The AI will have its palace moved for free here
tNewCapitals = ( 
	(21, 63), # Byzantines: Constantinople (restoration)
	(-1, -1), # -
	(-1, -1), # -
	(-1, -1), # -
	(-1, -1), # -
	(89, 59), # Samanids: Bukhara
	(-1, -1), # -
	(-1, -1), # -
	(-1, -1), # -
	(-1, -1), # -
	(-1, -1), # -
	(-1, -1), # -
	(-1, -1), # -
	(-1, -1), # -
	(-1, -1), # -
	(21, 63), # Rum: Constantinople
	(-1, -1), # -
	(36, 50), # Antioch: Antioch
	(33, 35), # Crusaders: Jerusalem
	(-1, -1), # -
	(111, 33), # Ghorids: Delhi
	(-1, -1), # -
	(37, 43), # Ayyubids: Damascus
	(24, 31), # Mamluks: Cairo
	(21, 63), # Ottomans: Constantinople
	(-1, -1), # -
	(85, 44), # Timurids: Herat
	(55, 54), # Ak Koyunlu: Tabriz
	(64, 39), # Safavids: Esfahan
	(106, 3), # Portugal: Goa
	(112, 29), # Mughals: Agra
) 

# CIVILIZATION DATA

tBirth = ( # starting year (these correspond to both to civilizations in the XML and players in WBSave, excluding Minors/Barbarians!)
	750, 750, 750, 750, 800, 819, 861, 898, 934, 942, 963, 969, 1008,1011,1037,1072,1077,1097,1099,1127,1148,1154,1169,1250,1300,1347,1370,1402,1501,1510,1526,750, 750, 1206,1250,1080,1506)
#	BYZ  MAK  ABB  CHA  MAL  SAM  ARM  YEM  BUY  GUJ  GHA  FAT  GEO  SIN  SEL  TUR  KHW  ANT  JER  ZEN  GHO  OMA  AYY  MAM  OTT  BAH  TIM  AKK  SAF  POR  MUG  IND  BAR  DEL  KAR  CIL  SHA

tVictory = ( # estimated time of historical victory for final score calculation
	1500,1300,1250,1400,1300,1140,1330,1500,1200,1240,1300,1250,1330,1330,1300,1460,1350,1290,1290,1400,1400,1600,1500,1500,1660,1700,1500,1500,1700,1700,1650)
#	BYZ  MAK  ABB  CHA  MAL  SAM  ARM  YEM  BUY  GUJ  GHA  FAT  GEO  SIN  SEL  TUR  KHW  ANT  JER  ZEN  GHO  OMA  AYY  MAM  OTT  BAH  TIM  AKK  SAF  POR  MUG

tDifference = ( # for not allowing new civ popup if too close
	  1,   1,   1,   1,   2,   2,   1,   3,   3,   3,   3,   1,   1,   2,   2,   2,   3,   2,   1,   2,   2,   1,   1,   0,   0,   1,   1,   0,   2,   1,   0)
#	BYZ  MAK  ABB  CHA  MAL  SAM  ARM  YEM  BUY  GUJ  GHA  FAT  GEO  SIN  SEL  TUR  KHW  ANT  JER  ZEN  GHO  OMA  AYY  MAM  OTT  BAH  TIM  AKK  SAF  POR  MUG

tRespawn = ( # one-off historical respawn
   1261,   0,1157,   0,1392,   0,1080,   0,   0,1380,   0,   0,1314,1339,   0,1250,1511,   0,1192,   0,1206,1624,   0,1382,1413,   0,   0,   0,   0,   0,   0)
#	BYZ  MAK  ABB  CHA  MAL  SAM  ARM  YEM  BUY  GUJ  GHA  FAT  GEO  SIN  SEL  TUR  KHW  ANT  JER  ZEN  GHO  OMA  AYY  MAM  OTT  BAH  TIM  AKK  SAF  POR  MUG

tFall = ( # a bit of determinism: no resurrection & stability penalty (if negative) beyond this point
   1330,1317,1258,2000,1562, 999,2000,2000,1055,1573,1187,1171,1460,1524,1194,1307,1231,1268,1291,1250,1526,2000,1341,1517,2000,1527,1526,1508,2000,2000,2000)
#	BYZ  MAK  ABB  CHA  MAL  SAM  ARM  YEM  BUY  GUJ  GHA  FAT  GEO  SIN  SEL  TUR  KHW  ANT  JER  ZEN  GHO  OMA  AYY  MAM  OTT  BAH  TIM  AKK  SAF  POR  MUG

tFallRespawned = ( # slight changes for respawned civs
   1330,1317,1258,2000,1562, 999,2000,2000,1055,1573,1187,1171,1460,1524,1194,1487,2000,1268,1489,1250,1526,2000,1341,1517,2000,1527,1526,1508,2000,2000,2000)
#	BYZ  MAK  ABB  CHA  MAL  SAM  ARM  YEM  BUY  GUJ  GHA  FAT  GEO  SIN  SEL  TUR  KHW  ANT  JER  ZEN  GHO  OMA  AYY  MAM  OTT  BAH  TIM  AKK  SAF  POR  MUG

tNoSettler = ( # 1 = civs that spawn without a settler (invasions)
	  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  0,  0,  1,  1,  1,  0,  1,  0,  0,  0,  0)
# 	BYZ MAK ABB CHA MAL SAM ARM YEM BUY GUJ GHA FAT GEO SIN SEL RUM KHW ANT JER ZEN GHO OMA AYY MAM OTT BAH TIM AKK SAF POR MUG 

tStartingGold = (
	750, 50,100,100,100,100,100,100,300,100,200,200,200,200,200,300,300,500,500,600,400,500,500,500,600,600,600,500,800,1000,800,100,100,100,100,100)
# 	BYZ MAK ABB CHA MAL SAM ARM YEM BUY GUJ GHA FAT GEO SIN SEL RUM KHW ANT JER ZEN GHO OMA AYY MAM OTT BAH TIM AKK SAF POR  MUG IN1 IN2 IN3 IN4 BAR

tResurrectionProb = ( # chance for a civ to be randomly respawned when there is a free slot
	 40, 30, 40, 60, 60,  0, 60, 50,  0, 60,  0,  0, 60, 50,  0, 20,  0,  0, 50,  0, 60, 50,  0, 80, 80, 40, 40,  0, 80,  0, 80)
#	BYZ MAK ABB CHA MAL SAM ARM YEM BUY GUJ GHA FAT GEO SIN SEL TUR KHW ANT JER ZEN GHO OMA AYY MAM OTT BAH TIM AKK SAF POR MUG

tAIStopBirthThreshold = (
	 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 100, 100, 100, 100, 100)
#	BYZ MAK ABB CHA MAL SAM ARM YEM BUY GUJ GHA FAT GEO SIN SEL TUR KHW ANT JER ZEN GHO OMA AYY MAM OTT BAH TIM AKK SAF POR MUG IN1 IN2 IN3 IN4 BAR

tReligiousTolerance = ( # 80: zoroastrians, 60: jews, 50: muslims/christians/hindu+buddhism, 10: catholic/orthodox, shia/sunni
	 60, 60, 60, 50, 60, 80, 60, 50, 80, 60, 10, 80, 60, 60, 60, 50, 60, 50, 50, 50, 10, 60, 60, 50, 10, 80, 10, 60, 10, 80, 80, 100, 100, 100, 100, 100)
#	BYZ MAK ABB CHA MAL SAM ARM YEM BUY GUJ GHA FAT GEO SIN SEL TUR KHW ANT JER ZEN GHO OMA AYY MAM OTT BAH TIM AKK SAF POR MUG IN1 IN2 IN3 IN4 BAR

tMassacreProb = ( # Probability of the AI massacring the non-state religion population upon city conquest
	  0,  0,  5,  5,  5,  5,  5, 25,  0,  5, 25,  0,  5,  0,  5, 40,  5, 50, 40, 40, 40, 15,  5,  5, 25,  5, 80,  5, 25,  0,  0,  0,  0,  0,  0, 40)
#	BYZ MAK ABB CHA MAL SAM ARM YEM BUY GUJ GHA FAT GEO SIN SEL TUR KHW ANT JER ZEN GHO OMA AYY MAM OTT BAH TIM AKK SAF POR MUG IN1 IN2 IN3 IN4 BAR

tBuildPersecutorProb = ( # Probability of the AI building a Religious Persecutor whenever it wants to build a missionary or spy
	 10,  5, 10,  5,  5,  5,  5, 15,  0,  5, 15,  0,  5,  5,  5, 25, 10, 25, 25, 25, 15, 15, 10, 15, 15,  0, 10,  5, 25,  5,  0,  0,  0,  0,  0,  0)
#	BYZ MAK ABB CHA MAL SAM ARM YEM BUY GUJ GHA FAT GEO SIN SEL TUR KHW ANT JER ZEN GHO OMA AYY MAM OTT BAH TIM AKK SAF POR MUG IN1 IN2 IN3 IN4 BAR

tHire = ( # Mercenaries (more = higher chance to hire a mercenary)
	 80, 50, 50, 50, 50, 80, 50, 50, 80, 50, 60, 70, 50, 50, 50, 50, 50, 80,100, 80, 70, 60, 50, 50, 20, 70, 20, 20, 50, 60, 50)
#	BYZ MAK ABB CHA MAL SAM ARM YEM BUY GUJ GHA FAT GEO SIN SEL TUR KHW ANT JER ZEN GHO OMA AYY MAM OTT BAH TIM AKK SAF POR MUG

tInflationPercent = (
	120,100,100,100, 97, 96, 92, 89, 87, 86, 83, 83, 80, 79, 77, 73, 72, 70, 70, 67, 64, 63, 65, 70, 45, 44, 42, 40, 31, 30, 28)
# 	BYZ MAK ABB CHA MAL SAM ARM YEM BUY GUJ GHA FAT GEO SIN SEL RUM KHW ANT JER ZEN GHO OMA AYY MAM OTT BAH TIM AKK SAF POR MUG

tGrowthPercent = (
	200,150,175,175,175,140,165,140,130,135,130,140,135,132,125,135,100,140,140,115,120,160,130,150, 75, 80, 90, 90, 50,150, 80,150,150,150,150,150)
# 	BYZ MAK ABB CHA MAL SAM ARM YEM BUY GUJ GHA FAT GEO SIN SEL RUM KHW ANT JER ZEN GHO OMA AYY MAM OTT BAH TIM AKK SAF POR MUG IN1 IN2 IN3 IN4 BAR

tProductionPercent = (
	200,145,140,135,130,130,150,130,120,125,120,120,115,120,120,135,100,110,110,105,100,125,105,130, 90, 85, 95, 85, 65, 110, 80)
# 	BYZ MAK ABB CHA MAL SAM ARM YEM BUY GUJ GHA FAT GEO SIN SEL RUM KHW ANT JER ZEN GHO OMA AYY MAM OTT BAH TIM AKK SAF POR MUG IN1 IN2 IN3 IN4 BAR

tResearchPercent = (
	180,160,145,160,150,125,130,125,140,135,120,120,120,130,130,130,112,125,125,120,110,145,110,160, 80, 80, 95, 95, 65, 85, 80)
# 	BYZ MAK ABB CHA MAL SAM ARM YEM BUY GUJ GHA FAT GEO SIN SEL RUM KHW ANT JER ZEN GHO OMA AYY MAM OTT BAH TIM AKK SAF POR MUG IN1 IN2 IN3 IN4 BAR

tEspionagePercent = (
	135,135,135,135,133,132,128,126,124,123,121,121,118,116,113,112,112,110,110,107,105,105,103,110, 90, 88, 86, 85, 80,100, 80)
# 	BYZ MAK ABB CHA MAL SAM ARM YEM BUY GUJ GHA FAT GEO SIN SEL RUM KHW ANT JER ZEN GHO OMA AYY MAM OTT BAH TIM AKK SAF POR MUG IN1 IN2 IN3 IN4 BAR

tGreatPeoplePercent = (
	130,115,110,110,110,110,110,110,110,105,100,115,100,100,100,100,100,100,100,100,100,110,110,110, 90,100, 90, 90, 75,200, 75,200,200,200,200,200)
# 	BYZ MAK ABB CHA MAL SAM ARM YEM BUY GUJ GHA FAT GEO SIN SEL RUM KHW ANT JER ZEN GHO OMA AYY MAM OTT BAH TIM AKK SAF POR MUG IN1 IN2 IN3 IN4 BAR

tCulturePercent = (
	 100, 85, 90, 90, 90, 90, 90,100,100,105, 90,108,110,110,100,105,120,100,100,115,128,100,130,125,150,150,150,133,175,100,165, 30, 30, 30, 30, 30)
# 	BYZ MAK ABB CHA MAL SAM ARM YEM BUY GUJ GHA FAT GEO SIN SEL RUM KHW ANT JER ZEN GHO OMA AYY MAM OTT BAH TIM AKK SAF POR MUG IN1 IN2 IN3 IN4 BAR

tNumCitiesMaintenancePercent = (
	 60,100,100,100,110,100,100, 95, 90, 93, 87, 92, 90, 90, 85, 95, 90, 95, 90, 84, 82, 92, 80, 90, 66, 72, 76, 70, 60,100, 65, 20, 20, 20, 20, 20)
# 	BYZ MAK ABB CHA MAL SAM ARM YEM BUY GUJ GHA FAT GEO SIN SEL RUM KHW ANT JER ZEN GHO OMA AYY MAM OTT BAH TIM AKK SAF POR MUG IN1 IN2 IN3 IN4 BAR

tDistanceMaintenancePercent = (
	60,100,100,100,115, 98,106,115, 90, 93, 87, 92, 95, 95, 95,100, 65, 95, 90, 94, 82, 62, 80,105, 66, 82, 51, 70, 60, 30, 65,  0,  0,  0,  0,  0)
# 	BYZ MAK ABB CHA MAL SAM ARM YEM BUY GUJ GHA FAT GEO SIN SEL RUM KHW ANT JER ZEN GHO OMA AYY MAM OTT BAH TIM AKK SAF POR MUG IN1 IN2 IN3 IN4 BAR

tCompactEmpireModifier = ( # higher values = more compact empire
	 25, 40, 30, 50, 50, 20, 50, 50, 30, 50, 30, 40, 50, 50, 20, 40, 20, 50, 50, 50, 30, 20, 40, 40, 30, 50, 20, 30, 40, 10, 40)
#	BYZ MAK ABB CHA MAL SAM ARM YEM BUY GUJ GHA FAT GEO SIN SEL TUR KHW ANT JER ZEN GHO OMA AYY MAM OTT BAH TIM AKK SAF POR MUG

tMaxTakenTiles = ( # Threshold for tiles occupied by other civs when founding new cities (AI); BTS Default = 7, RFC = 9-13
	  7, 11,  7,  9,  9,  7,  9,  7,  7,  9,  7,  9, 11,  9,  7, 11,  7, 13, 13, 13, 11,  9,  9, 11, 13, 11, 11, 13, 13, 13, 13)
#	BYZ MAK ABB CHA MAL SAM ARM YEM BUY GUJ GHA FAT GEO SIN SEL TUR KHW ANT JER ZEN GHO OMA AYY MAM OTT BAH TIM AKK SAF POR MUG

tWarDistanceModifier = ( # 1 = default, 2 = medium, 3 = far (civs are normally less likely to go at war with distant enemies)
	  1,  1,  2,  1,  1,  2,  1,  1,  1,  1,  1,  1,  1,  1,  2,  1,  2,  1,  1,  1,  1,  2,  1,  1,  1,  1,  3,  1,  1,  3,  1)
#	BYZ MAK ABB CHA MAL SAM ARM YEM BUY GUJ GHA FAT GEO SIN SEL TUR KHW ANT JER ZEN GHO OMA AYY MAM OTT BAH TIM AKK SAF POR MUG

tWarCoastalModifier = ( # AI wars: city evaluation bonus for coastal cities (default is 1)
	  2,  0,  1,  0,  0,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  2,  2,  1,  1,  3,  1,  1,  1,  1,  1,  0,  1,  2,  1)
#	BYZ MAK ABB CHA MAL SAM ARM YEM BUY GUJ GHA FAT GEO SIN SEL TUR KHW ANT JER ZEN GHO OMA AYY MAM OTT BAH TIM AKK SAF POR MUG

tLoadingTime = ( # estimated loading time shown on the civ-selection screen (these correspond to civilizations in the XML)
	  0,  0,  0,  0,  1,  1,  1,  2,  3,  3,  3,  3,  4,  4,  5,  6,  6,  8,  8, 10, 10, 10, 12, 25, 30, 30, 35, 35, 45, 45, 45)
# 	BYZ MAK ABB CHA MAL SAM ARM YEM BUY GUJ GHA FAT GEO SIN SEL RUM KHW ANT JER ZEN GHO OMA AYY MAM OTT BAH TIM AKK SAF POR MUG 

# Number of stars shown on the civ-selection screen & civilopedia (these correspond to civilizations in the XML);
# There is no formula for this and it's only meant to show the relative difficulty to the human player.
# Columns: 
# 	1. Trade (based on Maintenance modifiers, Research modifier and access to Companies)
# 	2. Production (based Production modifier)
# 	3. Culture (based Culture modifier)
# 	4. Growth (based on Growth modifier and food availability in starting area)
# 	5. Starting Situation (based on starting year, lands, neighbors, units)
tRating = (
	(2, 1, 3, 1, 5), # BYZ (12)
	(2, 1, 2, 3, 3), # MAK (11)
	(3, 2, 3, 2, 5), # ABB (16)
	(1, 2, 3, 2, 4), # CHA (12)
	(2, 2, 3, 2, 4), # MAL (13)
	(2, 3, 2, 3, 3), # SAM (13)
	(2, 2, 2, 2, 4), # ARM (12)
	(2, 3, 3, 3, 2), # YEM (13)
	(2, 3, 2, 3, 4), # BUY (14)
	(2, 3, 3, 3, 4), # GUJ (15)
	(4, 3, 1, 3, 3), # GHA (14)
	(3, 3, 3, 3, 4), # FAT (16)
	(3, 4, 3, 3, 3), # GEO (16)
	(1, 3, 3, 3, 4), # SIN (14)
	(2, 3, 2, 3, 4), # SEL (14)
	(2, 2, 2, 2, 3), # RUM (11)
	(4, 4, 3, 3, 2), # KHW (16)
	(2, 2, 2, 1, 2), # ANT (9)
	(3, 2, 2, 1, 2), # JER (10)
	(1, 3, 2, 3, 2), # ZEN (11)
	(2, 4, 3, 2, 2), # GHO (13)
	(3, 2, 1, 1, 4), # OMA (11)
	(3, 3, 3, 3, 3), # AYY (15)
	(3, 3, 2, 3, 5), # MAM (16)
	(5, 4, 4, 5, 2), # OTT (20)
	(2, 4, 3, 4, 1), # BAH (14)
	(4, 3, 3, 3, 3), # TIM (16)
	(3, 4, 2, 4, 1), # AKK (14)
	(4, 4, 4, 4, 2), # SAF (19)
	(5, 5, 2, 4, 2), # POR (18)
	(4, 4, 4, 4, 3), # MUG (19)
	(1, 1, 1, 1, 1), # Rebels
	(1, 1, 1, 1, 1), # Barbs
	(2, 4, 3, 2, 3), # Delhi
	(2, 2, 2, 2, 1), # Karaman
	(2, 2, 2, 2, 1), # Cilicia
	(4, 4, 3, 3, 1), # Shaybanids
)

# How fast a religion spreads within this civ's borders (default=100%); (was civSpreadFactor in CvRhyes.cpp)
tReligionSpreadPercent = (
#		JUD	 ZOR  HIN  BUD  CAT  ORT  SUN  SHI
	(	100,  50,  10,  10, 100, 250, 100, 100 ), # BYZ
	(	100,  20,  10,  10, 100, 250, 100, 100 ), # MAK
	(	100, 100,  10,  10,  80,  80, 250, 160 ), # ABB
	(	 50, 100, 200, 110,  10,  20, 100, 100 ), # CHA
	(	 50, 100, 150, 125,  10,  20, 150, 160 ), # MAL
	(	100, 150,  80, 100,  50,  80, 150, 100 ), # SAM
	(	100, 100,  10,  10, 150, 150, 100, 100 ), # ARM
	(	120,  80,  10,  10,  40,  50, 150, 270 ), # YEM
	(	100, 125,  80, 100,  50, 100, 150, 150 ), # BUY
	(	120, 200, 200, 125,  40,  50, 250, 100 ), # GUJ
	(	 50, 100,  80,  80,  10,  50, 150, 100 ), # GHA
	(	150, 120,  20,  20, 120, 120, 150, 170 ), # FAT
	(	100,  50,  10,  10, 100, 200, 100, 130 ), # GEO
	(	100, 100, 150,  80,  20,  80, 150, 180 ), # SIN
	(	100, 100,  60,  60,  40,  80, 200, 140 ), # SEL
	(	100,  50,  10,  10,  40,  40, 250, 100 ), # RUM
	(	100, 100,  20,  80,  10,  50, 200, 100 ), # KHW
	(	 90,  50,  10,  20, 100, 100,  80,  80 ), # ANT
	(	 90,  50,  10,  20, 100, 100, 100,  80 ), # JER
	(	100,  50,  20,  20,  50,  80, 250, 100 ), # ZEN
	(	 50, 100, 100,  60,  10,  20, 250, 100 ), # GHO
	(	 80,  80,  20,  20,  20,  80, 250, 160 ), # OMA
	(	 90,  50,  10,  10,  50,  80, 200, 100 ), # AYY
	(	 90,  20,  10,  10,  60,  90, 200, 100 ), # MAM
	(	 80,  20,  10,  10,  50,  70, 400,  80 ), # OTT
	(	100,  80, 120, 100,  80,  80, 250, 170 ), # BAH
	(	 60,  60,  60,  60,  60,  80, 250,  60 ), # TIM
	(	100, 100,  10,  10, 100, 100, 100, 220 ), # AKK
	(	 80,  80,  10,  10,  10,  50,  80, 420 ), # SAF
	(	100, 100, 100, 100, 120, 100,  80,  80 ), # POR
	(	100, 100, 120, 110, 100, 100, 200, 120 ), # MUG
	(	120, 120, 100, 120, 100, 100, 100, 110 ), # IN1
	(	120, 120, 100, 120, 100, 100, 100, 110 ), # IN2
	(	120, 120, 100, 120, 100, 100, 100, 110 ), # IN3
	(	120, 120, 100, 120, 100, 100, 100, 110 ), # IN4
	(	100, 100, 100, 120, 100, 100, 100, 120 )) # BAR

tBorders = (
# 
#		0-3 = no contact scrambling, 4 = low chance of cutting contact, 5 = high chance of cutting contact + no vassalage
#
# 		BYZ MAK ABB CHA MAL SAM ARM YEM BUY GUJ GHA FAT GEO SIN SEL RUM KHW ANT JER ZEN GHO OMA AYY MAM OTT BAH TIM AKK SAF POR MUG
# BYZ
	(	 0,  4,  1,  5,  5,  5,  1,  5,  5,  5,  5,  2,  2,  5,  2,  1,  5,  1,  1,  3,  5,  5,  2,  2,  1,  5,  4,  3,  3,  4,  5 ),
# MAK
	(	 4,  0,  2,  5,  5,  5,  5,  4,  5,  5,  5,  1,  5,  5,  5,  5,  5,  5,  4,  5,  5,  5,  1,  1,  5,  5,  5,  5,  5,  3,  5 ),
# ABB
	(	 1,  2,  0,  5,  5,  3,  1,  1,  1,  5,  3,  1,  2,  4,  1,  3,  4,  1,  1,  1,  4,  1,  1,  1,  3,  5,  3,  1,  3,  5,  4 ),
# CHA
	(	 5,  5,  5,  0,  1,  4,  5,  5,  5,  1,  2,  5,  5,  1,  5,  5,  4,  5,  5,  5,  1,  4,  5,  5,  5,  2,  4,  5,  4,  5,  1 ),
# MAL
	(	 5,  5,  5,  1,  0,  5,  5,  5,  5,  1,  2,  5,  5,  2,  5,  5,  4,  5,  5,  5,  1,  4,  5,  5,  5,  1,  4,  5,  4,  5,  1 ),
# SAM
	(	 5,  5,  3,  4,  5,  0,  5,  5,  1,  5,  1,  5,  5,  5,  2,  5,  1,  5,  5,  5,  1,  5,  5,  5,  5,  5,  1,  3,  2,  5,  4 ),
# ARM
	(	 1,  5,  1,  5,  5,  5,  0,  5,  4,  5,  5,  3,  1,  5,  2,  1,  5,  1,  1,  4,  5,  5,  3,  3,  1,  5,  4,  4,  3,  5,  5 ),
# YEM
	(	 5,  4,  1,  5,  5,  5,  5,  0,  5,  5,  5,  2,  5,  5,  5,  5,  5,  5,  4,  4,  5,  4,  2,  3,  4,  5,  5,  5,  5,  5,  5 ),
# BUY
	(	 5,  5,  1,  5,  5,  1,  4,  5,  0,  5,  2,  4,  4,  5,  1,  5,  1,  5,  5,  4,  4,  3,  5,  5,  5,  5,  2,  4,  1,  5,  5 ),
# GUJ
	(	 5,  5,  5,  1,  1,  5,  5,  5,  5,  0,  2,  5,  5,  1,  5,  5,  4,  5,  5,  5,  2,  3,  5,  5,  5,  1,  4,  5,  5,  5,  1 ),
# GHA
	(	 5,  5,  3,  2,  2,  1,  5,  5,  2,  2,  0,  5,  5,  1,  3,  5,  3,  5,  5,  5,  1,  5,  5,  5,  5,  5,  3,  5,  4,  5,  3 ),
# FAT
	(	 2,  1,  1,  5,  5,  5,  3,  2,  4,  5,  5,  0,  4,  4,  2,  3,  5,  1,  1,  4,  5,  5,  1,  1,  1,  5,  4,  4,  4,  5,  5 ),
# GEO
	(	 2,  5,  2,  5,  5,  5,  1,  5,  4,  5,  5,  4,  0,  5,  2,  2,  5,  3,  4,  4,  5,  5,  4,  4,  2,  5,  4,  4,  2,  5,  5 ),
# SIN
	(	 5,  5,  4,  1,  2,  5,  5,  5,  5,  1,  1,  4,  5,  0,  5,  5,  5,  5,  5,  5,  3,  4,  5,  5,  5,  2,  4,  5,  4,  5,  2 ),
# SEL
	(	 2,  5,  1,  5,  5,  2,  2,  5,  1,  5,  3,  2,  2,  5,  0,  1,  3,  1,  1,  1,  4,  5,  3,  3,  1,  5,  3,  1,  1,  5,  5 ),
# RUM
	(	 1,  5,  3,  5,  5,  5,  1,  5,  5,  5,  5,  3,  2,  5,  1,  0,  5,  2,  2,  2,  5,  5,  3,  3,  1,  5,  4,  4,  4,  5,  5 ),
# KHW
	(	 5,  5,  4,  4,  4,  1,  5,  5,  1,  5,  3,  5,  5,  5,  3,  5,  0,  5,  5,  4,  3,  5,  5,  5,  5,  5,  1,  2,  1,  5,  4 ),
# ANT
	(	 1,  5,  1,  5,  5,  5,  1,  5,  5,  5,  5,  1,  3,  5,  1,  2,  5,  0,  1,  1,  5,  5,  1,  1,  1,  5,  4,  4,  4,  4,  5 ),
# JER
	(	 1,  5,  1,  5,  5,  5,  1,  4,  5,  5,  5,  1,  4,  5,  1,  2,  5,  1,  0,  1,  5,  5,  1,  1,  1,  5,  4,  4,  4,  4,  5 ),
# ZEN
	(	 4,  5,  1,  5,  5,  5,  4,  5,  4,  4,  5,  4,  4,  5,  1,  2,  4,  1,  1,  0,  5,  5,  1,  2,  4,  5,  5,  1,  4,  5,  5 ),
# GHO
	(	 5,  5,  4,  1,  1,  1,  5,  5,  4,  2,  1,  5,  5,  3,  4,  5,  3,  5,  5,  5,  0,  5,  5,  5,  5,  2,  2,  4,  3,  5,  1 ),
# OMA
	(	 5,  5,  1,  4,  4,  5,  5,  4,  3,  4,  5,  5,  5,  4,  5,  5,  5,  5,  5,  5,  5,  0,  5,  5,  4,  4,  5,  5,  4,  5,  5 ),
# AYY
	(	 2,  1,  1,  5,  5,  5,  3,  2,  5,  5,  5,  1,  4,  5,  3,  3,  5,  1,  1,  1,  5,  5,  0,  1,  2,  5,  5,  4,  4,  5,  5 ),
# MAM
	(	 2,  1,  1,  5,  5,  5,  3,  3,  5,  5,  5,  1,  4,  5,  3,  3,  5,  1,  1,  2,  5,  5,  1,  0,  1,  5,  5,  4,  4,  5,  5 ),
# OTT
	(	 1,  5,  3,  5,  5,  5,  1,  4,  5,  5,  5,  3,  2,  5,  1,  1,  5,  1,  1,  4,  5,  4,  2,  1,  0,  5,  4,  4,  1,  4,  5 ),
# BAH
	(	 5,  5,  5,  2,  1,  5,  5,  5,  5,  1,  5,  5,  5,  2,  5,  5,  5,  5,  5,  5,  2,  4,  5,  5,  5,  0,  5,  5,  5,  4,  1 ),
# TIM
	(	 4,  5,  3,  4,  4,  1,  4,  5,  2,  4,  3,  4,  4,  4,  3,  4,  1,  4,  4,  5,  2,  5,  5,  5,  4,  5,  0,  1,  1,  5,  3 ),
# AKK
	(	 4,  5,  1,  5,  5,  3,  4,  5,  4,  5,  5,  4,  4,  5,  1,  4,  2,  4,  4,  1,  4,  5,  4,  4,  4,  5,  1,  0,  1,  5,  5 ),
# SAF
	(	 4,  5,  3,  4,  4,  2,  3,  5,  1,  5,  4,  4,  2,  4,  1,  4,  1,  4,  4,  4,  3,  4,  4,  4,  1,  5,  1,  1,  0,  4,  2 ),
# POR
	(	 4,  3,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  4,  4,  5,  5,  5,  5,  4,  4,  4,  5,  5,  4,  0,  5 ),
# MUG
	(	 5,  5,  4,  1,  1,  4,  5,  5,  5,  1,  3,  5,  5,  2,  5,  5,  4,  5,  5,  5,  1,  5,  5,  5,  5,  1,  3,  5,  2,  4,  0 ))
#  		BYZ MAK ABB CHA MAL SAM ARM YEM BUY GUJ GHA FAT GEO SIN SEL RUM KHW ANT JER ZEN GHO OMA AYY MAM OTT BAH TIM AKK SAF POR MUG

# Permanent modifiers to attitude of civ vs civ
tAttitudeModifier = (
#  		BYZ MAK ABB CHA MAL SAM ARM YEM BUY GUJ GHA FAT GEO SIN SEL RUM KHW ANT JER ZEN GHO OMA AYY MAM OTT BAH TIM AKK SAF POR MUG
# BYZ
	(	 0,  1, -1,  0,  0,  0,  1, -1,  0,  0,  0,  0,  1,  0, -2, -2,  0, -1, -1, -1, -1,  0,  0,  0, -2,  0, -1,  0,  0,  1,  0 ),
# MAK
	(	 1,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ),
# ABB
	(	-1,  1,  0,  0,  0,  1, -1,  0, -2,  0,  0, -1,  0,  0,  0,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ),
# CHA
	(	 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ),
# MAL
	(	 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ),
# SAM
	(	 0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ),
# ARM
	(	 1,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ),
# YEM
	(	-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ),
# BUY
	(	 0,  0, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ),
# GUJ
	(	 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ),
# GHA
	(	 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ),
# FAT
	(	 0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ),
# GEO
	(	 1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ),
# SIN
	(	 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ),
# SEL
	(	-2,  0,  0,  0,  0,  0, -1,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ),
# RUM
	(	-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0 ),
# KHW
	(	 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2,  0,  0,  0, -1 ),
# ANT
	(	-1,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0 ),
# JER
	(	-1,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0 ),
# ZEN
	(	-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ),
# GHO
	(	-1,  0,  0, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1 ),
# OMA
	(	 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ),
# AYY
	(	 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ),
# MAM
	(	 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ),
# OTT
	(	-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ),
# BAH
	(	 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ),
# TIM
	(	-1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  0, -1, -1, -1,  0,  0, -2, -1, -1,  0, -1, -1, -1, -1, -2,  0,  0,  0, -1, -1,  1 ),
# AKK
	(	 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ),
# SAF
	(	 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ),
# POR
	(	 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ),
# MUG
	(	 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0, -1,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0 ))
# 	 	BYZ MAK ABB CHA MAL SAM ARM YEM BUY GUJ GHA FAT GEO SIN SEL RUM KHW ANT JER ZEN GHO OMA AYY MAM OTT BAH TIM AKK SAF POR MUG
	
# Names and descriptions of civilizations' Unique Powers
tUniquePowers = (
	("TXT_KEY_UP_BYZ", "TXT_KEY_UP_BYZ2"),
	("TXT_KEY_UP_MAK", "TXT_KEY_UP_MAK2"),
	("TXT_KEY_UP_ABB", "TXT_KEY_UP_ABB2"),
	("TXT_KEY_UP_CHA", "TXT_KEY_UP_CHA2"),
	("TXT_KEY_UP_MAL", "TXT_KEY_UP_MAL2"),
	("TXT_KEY_UP_SAM", "TXT_KEY_UP_SAM2"),
	("TXT_KEY_UP_ARM", "TXT_KEY_UP_ARM2"),
	("TXT_KEY_UP_YEM", "TXT_KEY_UP_YEM2"),
	("TXT_KEY_UP_BUY", "TXT_KEY_UP_BUY2"),
	("TXT_KEY_UP_GUJ", "TXT_KEY_UP_GUJ2"),
	("TXT_KEY_UP_GHA", "TXT_KEY_UP_GHA2"),
	("TXT_KEY_UP_FAT", "TXT_KEY_UP_FAT2"),
	("TXT_KEY_UP_GEO", "TXT_KEY_UP_GEO2"),
	("TXT_KEY_UP_SIN", "TXT_KEY_UP_SIN2"),
	("TXT_KEY_UP_SEL", "TXT_KEY_UP_SEL2"),
	("TXT_KEY_UP_RUM", "TXT_KEY_UP_RUM2"),
	("TXT_KEY_UP_KHW", "TXT_KEY_UP_KHW2"),
	("TXT_KEY_UP_ANT", "TXT_KEY_UP_ANT2"),
	("TXT_KEY_UP_JER", "TXT_KEY_UP_JER2"),
	("TXT_KEY_UP_ZEN", "TXT_KEY_UP_ZEN2"),
	("TXT_KEY_UP_GHO", "TXT_KEY_UP_GHO2"),
	("TXT_KEY_UP_OMA", "TXT_KEY_UP_OMA2"),
	("TXT_KEY_UP_AYY", "TXT_KEY_UP_AYY2"),
	("TXT_KEY_UP_MAM", "TXT_KEY_UP_MAM2"),
	("TXT_KEY_UP_OTT", "TXT_KEY_UP_OTT2"),
	("TXT_KEY_UP_BAH", "TXT_KEY_UP_BAH2"),
	("TXT_KEY_UP_TIM", "TXT_KEY_UP_TIM2"),
	("TXT_KEY_UP_AKK", "TXT_KEY_UP_AKK2"),
	("TXT_KEY_UP_SAF", "TXT_KEY_UP_SAF2"),
	("TXT_KEY_UP_POR", "TXT_KEY_UP_POR2"),
	("TXT_KEY_UP_MUG", "TXT_KEY_UP_MUG2"),
)

# Descriptions for Unique Historical Victory goals, one set for each game speed & civ
tGoals = (
	( # Epic
		("TXT_KEY_UHV_BYZ1", "TXT_KEY_UHV_BYZ2", "TXT_KEY_UHV_BYZ3"),
		("TXT_KEY_UHV_MAK1", "TXT_KEY_UHV_MAK2", "TXT_KEY_UHV_MAK3"),
		("TXT_KEY_UHV_ABB1", "TXT_KEY_UHV_ABB2", "TXT_KEY_UHV_ABB3"),
		("TXT_KEY_UHV_CHA1", "TXT_KEY_UHV_CHA2", "TXT_KEY_UHV_CHA3"),
		("TXT_KEY_UHV_MAL1", "TXT_KEY_UHV_MAL2", "TXT_KEY_UHV_MAL3"),
		("TXT_KEY_UHV_SAM1", "TXT_KEY_UHV_SAM2", "TXT_KEY_UHV_SAM3"),
		("TXT_KEY_UHV_ARM1", "TXT_KEY_UHV_ARM2", "TXT_KEY_UHV_ARM3_EPIC"),
		("TXT_KEY_UHV_YEM1", "TXT_KEY_UHV_YEM2", "TXT_KEY_UHV_YEM3"),
		("TXT_KEY_UHV_BUY1", "TXT_KEY_UHV_BUY2", "TXT_KEY_UHV_BUY3"),
		("TXT_KEY_UHV_GUJ1", "TXT_KEY_UHV_GUJ2", "TXT_KEY_UHV_GUJ3"),
		("TXT_KEY_UHV_GHA1_EPIC", "TXT_KEY_UHV_GHA2", "TXT_KEY_UHV_GHA3_EPIC"),
		("TXT_KEY_UHV_FAT1", "TXT_KEY_UHV_FAT2", "TXT_KEY_UHV_FAT3"),
		("TXT_KEY_UHV_GEO1", "TXT_KEY_UHV_GEO2", "TXT_KEY_UHV_GEO3"),
		("TXT_KEY_UHV_SIN1", "TXT_KEY_UHV_SIN2", "TXT_KEY_UHV_SIN3"),
		("TXT_KEY_UHV_SEL1", "TXT_KEY_UHV_SEL2", "TXT_KEY_UHV_SEL3"),
		("TXT_KEY_UHV_TUR1", "TXT_KEY_UHV_TUR2", "TXT_KEY_UHV_TUR3"),
		("TXT_KEY_UHV_KHW1", "TXT_KEY_UHV_KHW2", "TXT_KEY_UHV_KHW3"),
		("TXT_KEY_UHV_ANT1", "TXT_KEY_UHV_ANT2", "TXT_KEY_UHV_ANT3"),
		("TXT_KEY_UHV_JER1", "TXT_KEY_UHV_JER2", "TXT_KEY_UHV_JER3"),
		("TXT_KEY_UHV_ZEN1", "TXT_KEY_UHV_ZEN2", "TXT_KEY_UHV_ZEN3"),
		("TXT_KEY_UHV_GHO1", "TXT_KEY_UHV_GHO2", "TXT_KEY_UHV_GHO3"),
		("TXT_KEY_UHV_OMA1", "TXT_KEY_UHV_OMA2_EPIC", "TXT_KEY_UHV_OMA3"),
		("TXT_KEY_UHV_AYY1", "TXT_KEY_UHV_AYY2", "TXT_KEY_UHV_AYY3"),
		("TXT_KEY_UHV_MAM1", "TXT_KEY_UHV_MAM2", "TXT_KEY_UHV_MAM3"),
		("TXT_KEY_UHV_OTT1", "TXT_KEY_UHV_OTT2", "TXT_KEY_UHV_OTT3"),
		("TXT_KEY_UHV_BAH1", "TXT_KEY_UHV_BAH2", "TXT_KEY_UHV_BAH3"),
		("TXT_KEY_UHV_TIM1", "TXT_KEY_UHV_TIM2", "TXT_KEY_UHV_TIM3"),
		("TXT_KEY_UHV_AKK1", "TXT_KEY_UHV_AKK2", "TXT_KEY_UHV_AKK3"),
		("TXT_KEY_UHV_SAF1", "TXT_KEY_UHV_SAF2", "TXT_KEY_UHV_SAF3"),
		("TXT_KEY_UHV_POR1", "TXT_KEY_UHV_POR2", "TXT_KEY_UHV_POR3_EPIC"),
		("TXT_KEY_UHV_MUG1", "TXT_KEY_UHV_MUG2", "TXT_KEY_UHV_MUG3"),
	),
	( # Normal
		("TXT_KEY_UHV_BYZ1", "TXT_KEY_UHV_BYZ2", "TXT_KEY_UHV_BYZ3"),
		("TXT_KEY_UHV_MAK1", "TXT_KEY_UHV_MAK2", "TXT_KEY_UHV_MAK3"),
		("TXT_KEY_UHV_ABB1", "TXT_KEY_UHV_ABB2", "TXT_KEY_UHV_ABB3"),
		("TXT_KEY_UHV_CHA1", "TXT_KEY_UHV_CHA2", "TXT_KEY_UHV_CHA3"),
		("TXT_KEY_UHV_MAL1", "TXT_KEY_UHV_MAL2", "TXT_KEY_UHV_MAL3"),
		("TXT_KEY_UHV_SAM1", "TXT_KEY_UHV_SAM2", "TXT_KEY_UHV_SAM3"),
		("TXT_KEY_UHV_ARM1", "TXT_KEY_UHV_ARM2", "TXT_KEY_UHV_ARM3"),
		("TXT_KEY_UHV_YEM1", "TXT_KEY_UHV_YEM2", "TXT_KEY_UHV_YEM3"),
		("TXT_KEY_UHV_BUY1", "TXT_KEY_UHV_BUY2", "TXT_KEY_UHV_BUY3"),
		("TXT_KEY_UHV_GUJ1", "TXT_KEY_UHV_GUJ2", "TXT_KEY_UHV_GUJ3"),
		("TXT_KEY_UHV_GHA1", "TXT_KEY_UHV_GHA2", "TXT_KEY_UHV_GHA3"),
		("TXT_KEY_UHV_FAT1", "TXT_KEY_UHV_FAT2", "TXT_KEY_UHV_FAT3"),
		("TXT_KEY_UHV_GEO1", "TXT_KEY_UHV_GEO2", "TXT_KEY_UHV_GEO3"),
		("TXT_KEY_UHV_SIN1", "TXT_KEY_UHV_SIN2", "TXT_KEY_UHV_SIN3"),
		("TXT_KEY_UHV_SEL1", "TXT_KEY_UHV_SEL2", "TXT_KEY_UHV_SEL3"),
		("TXT_KEY_UHV_TUR1", "TXT_KEY_UHV_TUR2", "TXT_KEY_UHV_TUR3"),
		("TXT_KEY_UHV_KHW1", "TXT_KEY_UHV_KHW2", "TXT_KEY_UHV_KHW3"),
		("TXT_KEY_UHV_ANT1", "TXT_KEY_UHV_ANT2", "TXT_KEY_UHV_ANT3"),
		("TXT_KEY_UHV_JER1", "TXT_KEY_UHV_JER2", "TXT_KEY_UHV_JER3"),
		("TXT_KEY_UHV_ZEN1", "TXT_KEY_UHV_ZEN2", "TXT_KEY_UHV_ZEN3"),
		("TXT_KEY_UHV_GHO1", "TXT_KEY_UHV_GHO2", "TXT_KEY_UHV_GHO3"),
		("TXT_KEY_UHV_OMA1", "TXT_KEY_UHV_OMA2", "TXT_KEY_UHV_OMA3"),
		("TXT_KEY_UHV_AYY1", "TXT_KEY_UHV_AYY2", "TXT_KEY_UHV_AYY3"),
		("TXT_KEY_UHV_MAM1", "TXT_KEY_UHV_MAM2", "TXT_KEY_UHV_MAM3"),
		("TXT_KEY_UHV_OTT1", "TXT_KEY_UHV_OTT2", "TXT_KEY_UHV_OTT3"),
		("TXT_KEY_UHV_BAH1", "TXT_KEY_UHV_BAH2", "TXT_KEY_UHV_BAH3"),
		("TXT_KEY_UHV_TIM1", "TXT_KEY_UHV_TIM2", "TXT_KEY_UHV_TIM3"),
		("TXT_KEY_UHV_AKK1", "TXT_KEY_UHV_AKK2", "TXT_KEY_UHV_AKK3"),
		("TXT_KEY_UHV_SAF1", "TXT_KEY_UHV_SAF2", "TXT_KEY_UHV_SAF3"),
		("TXT_KEY_UHV_POR1", "TXT_KEY_UHV_POR2", "TXT_KEY_UHV_POR3"),
		("TXT_KEY_UHV_MUG1", "TXT_KEY_UHV_MUG2", "TXT_KEY_UHV_MUG3"),
	)
)

# Descriptions for Unique Religious Victory goals, one set for each major religion
tReligiousGoals = (
	(" ", " ", " "), # Judaism
	(" ", " ", " "), # Zoroastrianism
	("TXT_KEY_URV_HINDUISM1", "TXT_KEY_URV_HINDUISM2", "TXT_KEY_URV_HINDUISM3"),
	(" ", " ", " "), # Buddhism
	("TXT_KEY_URV_CATHOLICISM1", "TXT_KEY_URV_CATHOLICISM2", "TXT_KEY_URV_CATHOLICISM3"),
	("TXT_KEY_URV_ORTHODOXY1", "TXT_KEY_URV_ORTHODOXY2", "TXT_KEY_URV_ORTHODOXY3"),
	("TXT_KEY_URV_SUNNI1", "TXT_KEY_URV_SUNNI2", "TXT_KEY_URV_SUNNI3"),
	("TXT_KEY_URV_SHIA1", "TXT_KEY_URV_SHIA2", "TXT_KEY_URV_SHIA3"),
)

# Civilizations that will be contact when the civ spawns
lContactCivsOnSpawn = [
	[], # Byzantium
	[], # Makuria
	[iByzantium], # Abbasids
	[], # Chauhan
	[], # Malwa
	[iAbbasids], # Samanids
	[iByzantium, iAbbasids], # Armenia
	[iAbbasids], # Yemen
	[iSamanids], # Buyids
	[iChauhan, iMalwa], # Gujarat
	[iAbbasids], # Ghaznavids
	[iAbbasids], # Fatimids
	[iByzantium, iArmenia], # Georgia
	[iAbbasids, iFatimids], # Sindh
	[iAbbasids], # Seljuks
	[iByzantium, iAbbasids, iArmenia, iSeljuks], # Rum
	[iAbbasids, iGhaznavids, iSeljuks], # Khwarezm
	[iByzantium, iArmenia], # Antioch
	[iByzantium, iArmenia, iAntioch], # Crusaders
	[iSeljuks, iRum, iAbbasids], # Zengids
	[iGhaznavids], # Ghorids
	[iAbbasids], # Oman
	[iMakuria, iAbbasids], # Ayyubids
	[iMakuria, iAbbasids, iAyyubids], # Mamluks
	[iByzantium, iAbbasids, iSeljuks, iRum, iArmenia, iGeorgia], # Ottomans
	[iGhorids], # Bahmanids
	[], # Timurids
	[iTimurids, iSeljuks, iRum], # Ak Koyunlu
	[iArmenia, iGeorgia, iAkKoyunlu], # Safavids
	[iByzantium, iMakuria], # Portugal
	[iTimurids, iGhaznavids, iSamanids, iGhorids, iChauhan, iGujarat, iMalwa, iSindh], # Mughals
]

# Guaranteed war on spawn
lEnemyCivsOnSpawn = [
	[], # Byzantium
	[], # Makuria
	[], # Abbasids
	[], # Chauhan
	[], # Malwa
	[], # Samanids
	[], # Armenia
	[], # Yemen
	[iAbbasids], # Buyids
	[], # Gujarat
	[iSamanids], # Ghaznavids
	[iAbbasids], # Fatimids
	[], # Georgia
	[], # Sindh
	[iByzantium, iArmenia, iGhaznavids, iBuyids], # Seljuks
	[iByzantium, iArmenia], # Rum
	[iSamanids], # Khwarezm
	[iAbbasids, iFatimids, iSeljuks, iRum], # Antioch
	[iAbbasids, iFatimids, iSeljuks, iRum], # Crusaders
	[iAntioch, iCrusaders], # Zengids
	[iSamanids, iGhaznavids], # Ghorids
	[], # Oman
	[iAntioch, iCrusaders, iZengids, iFatimids], # Ayyubids
	[iAntioch, iCrusaders, iFatimids, iAyyubids], # Mamluks
	[iByzantium], # Ottomans
	[], # Bahmanids
	[iKhwarezm, iSamanids, iSeljuks], # Timurids
	[], # Ak Koyunlu
	[iSeljuks], # Safavids
	[], # Portugal (war with Oman and Yemen in Barbs.py)
	[iGhorids], # Mughals
]

# Neighbours (unstable neighbors affect stability)
lNeighbours = [
	[iArmenia, iGeorgia, iRum, iOttomans], # Byzantium
	[iFatimids, iAyyubids, iMamluks, iYemen], # Makuria
	[iArmenia, iGeorgia, iOman, iSeljuks, iCrusaders, iAkKoyunlu, iZengids, iBuyids], # Abbasids
	[iMalwa, iGujarat, iGhorids, iMughals], # Chauhan
	[iChauhan, iGujarat, iGhorids, iMughals], # Malwa
	[iKhwarezm, iGhaznavids, iGhorids, iSeljuks, iTimurids, iSafavids, iBuyids], # Samanids
	[iByzantium, iAbbasids, iGeorgia, iSafavids], # Armenia
	[iMakuria, iFatimids, iAyyubids, iMamluks], # Yemen
	[iAbbasids, iSamanids, iOman, iSeljuks, iSafavids], # Buyids
	[iChauhan, iMalwa, iSindh, iMughals], # Gujarat
	[iGhorids, iChauhan, iSindh, iSamanids, iSeljuks], # Ghaznavids
	[iMakuria, iAbbasids, iCrusaders, iYemen, iAyyubids, iMamluks, iZengids], # Fatimids
	[iByzantium, iArmenia], # Georgia
	[iGujarat, iGhaznavids], # Sindh
	[iRum, iAbbasids, iCrusaders, iSafavids, iAkKoyunlu, iSamanids, iZengids, iGhaznavids, iBuyids, iOman], # Seljuks
	[iByzantium, iArmenia, iSeljuks, iZengids, iOttomans], # Rum
	[iTimurids, iSafavids, iSamanids], # Khwarezm
	[iAbbasids, iFatimids, iAyyubids, iMamluks, iRum, iZengids, iCrusaders], # Antioch
	[iAbbasids, iFatimids, iAyyubids, iMamluks, iRum, iZengids, iAntioch], # Crusaders
	[iAbbasids, iSeljuks, iRum, iAyyubids, iCrusaders, iMamluks, iFatimids], # Zengids
	[iGhaznavids, iChauhan, iSamanids], # Ghorids
	[iAbbasids, iBuyids, iSeljuks, iSafavids], # Oman
	[iAbbasids, iCrusaders, iMakuria, iYemen, iZengids, iMamluks, iFatimids], # Ayyubids
	[iAbbasids, iCrusaders, iMakuria, iYemen, iAyyubids, iFatimids], # Mamluks
	[iByzantium, iArmenia, iRum], # Ottomans
	[iGujarat, iMalwa, iMughals], # Bahmanids
	[iKhwarezm, iAkKoyunlu, iGhorids, iSamanids], # Timurids
	[iSeljuks, iAbbasids, iTimurids], # Ak Koyunlu
	[iAkKoyunlu, iSeljuks, iAbbasids, iArmenia, iKhwarezm, iSamanids, iOman, iBuyids], # Safavids
	[], # Portugal
	[iChauhan, iMalwa, iGujarat, iSindh, iGhorids, iBahmanids], # Mughals
]

# Used for stability hit on spawn (-3, double for -6)
lOlderNeighbours = [
	[], # Byzantium
	[], # Makuria
	[], # Abbasids
	[], # Chauhan
	[], # Malwa
	[iAbbasids], # Samanids
	[iAbbasids, iByzantium], # Armenia
	[iMakuria], # Yemen
	[iAbbasids, iSamanids], # Buyids
	[iChauhan], # Gujarat
	[iChauhan, iSamanids], # Ghaznavids
	[iAbbasids, iMakuria], # Fatimids
	[iByzantium], # Georgia
	[], # Sindh
	[iAbbasids, iByzantium, iSamanids, iBuyids, iGhaznavids], # Seljuks
	[iByzantium], # Rum
	[iSeljuks, iSamanids, iBuyids], # Khwarezm
	[iAbbasids, iRum], # Antioch
	[iAbbasids, iFatimids], # Crusaders
	[iCrusaders, iAntioch, iAbbasids, iSeljuks], # Zengids
	[iGhaznavids, iGhaznavids, iChauhan, iSindh, iSamanids], # Ghorids
	[iSeljuks], # Oman
	[iMakuria, iCrusaders, iAntioch, iYemen, iZengids, iZengids], # Ayyubids
	[iAbbasids, iMakuria, iZengids, iCrusaders, iAntioch], # Mamluks
	[iByzantium, iArmenia], # Ottomans
	[], # Bahmanids
	[iAbbasids, iKhwarezm, iKhwarezm, iSeljuks, iGhaznavids, iSamanids, iBuyids], # Timurids
	[iAbbasids, iSeljuks, iZengids], # Ak Koyunlu
	[iAbbasids, iArmenia, iGeorgia, iAkKoyunlu, iAkKoyunlu, iSeljuks, iSeljuks, iSamanids, iBuyids, iZengids], # Safavids
	[iChauhan, iMalwa, iGujarat, iSindh, iYemen, iOman], # Portugal
	[iChauhan, iMalwa, iGujarat, iSindh, iGhaznavids, iGhaznavids, iGhorids, iGhorids, iBahmanids], # Mughals
]

# RELIGIONS

iNumReligions = 8
(iJudaism, iZoroastrianism, iHinduism, iBuddhism, iCatholicism, iOrthodoxy, iSunni, iShia) = range(iNumReligions)

# The AI will persecute religions in this order, depending on its own state religion (one row per religion)
tPersecutionOrder = (
	(iZoroastrianism, iCatholicism, iOrthodoxy, iShia, iSunni, iHinduism, iBuddhism),
	(iSunni, iShia, iCatholicism, iOrthodoxy, iJudaism, iHinduism, iBuddhism),
	(iSunni, iShia, iCatholicism, iOrthodoxy, iZoroastrianism, iJudaism, iBuddhism),
	(iSunni, iShia, iZoroastrianism, iJudaism, iCatholicism, iOrthodoxy, iHinduism),
	(iJudaism, iZoroastrianism, iSunni, iShia, iHinduism, iOrthodoxy, iBuddhism),
	(iJudaism, iZoroastrianism, iSunni, iShia, iHinduism, iCatholicism, iBuddhism),
	(iShia, iHinduism, iZoroastrianism, iCatholicism, iOrthodoxy, iJudaism, iBuddhism),
	(iSunni, iHinduism, iZoroastrianism, iCatholicism, iOrthodoxy, iJudaism, iBuddhism),
)

# The amount of turns that must pass between holy war calls
iHolyWarPeriod = 100

# COMPANIES (CORPORATIONS)

iNumCompanies = 11
(iSufi, iKarimi, iNizari, iHospitallers, iTemplars, iVenetians, iGenoans, iPortuguese, iSilk, iPisans, iTamils) = range(iNumCompanies)

tCompaniesBirth = (850, 1050, 1088, 1099, 1099, 1099, 1099, 1507, 750, 1099, 750)
tCompaniesDeath = (2000, 2000, 1400, 2000, 1314, 2000, 2000, 2000, 1453, 2000, 1650)
tCompaniesLimit = (10, 10, 4, 5, 5, 12, 12, 11, 12, 12, 10)

# TITLES (PROJECTS)

iNumTitles = 6
(iRomanEmperor, iCaliph, iShahanshah, iSharif, iProtector, iRaja) = range(iNumTitles)

# CIVICS

iNumCivics = 25
(iTribalFederationCivic, iMonarchyCivic, iAristocracyCivic, iEmpireCivic, iAbsolutismCivic,
iTribalLawCivic, iVassalageCivic, iReligiousLawCivic, iBureacracyCivic, iMeritocracyCivic,
iTribalismCivic, iSlaveryCivic, iCasteSystemCivic, iSerfdomCivic, iFreeLaborCivic,
iDecentralizationCivic, iAgrarianismCivic, iMarketEconomyCivic, iMerchantCapitalismCivic, iStateMonopolyCivic,
iPaganismCivic, iOrganizedReligionCivic, iTheocracyCivic, iPersecutionCivic, iFreeReligionCivic) = range(iNumCivics)

# ERAS

iNumEras = 4
(iEra1, iEra2, iEra3, iEra4) = range(iNumEras)

# PROMOTIONS

iNumPromotions = 57
(iCombat1, iCombat2, iCombat3, iCombat4, iCombat5, iCombat6, iCover, iShock, iPinch, iFormation, iSkirmish, iCharge, iAmphibious, 
iMarch, iBlitz, iCommando, iMedic1, iMedic2, iMedic3, iGuerilla1, iGuerilla2, iGuerilla3, iWoodsman1, iWoodsman2, iWoodsman3, 
iCityRaider1, iCityRaider2, iCityRaider3, iCityGarrison1, iCityGarrison2, iCityGarrison3, iDrill1, iDrill2, iDrill3, iDrill4, 
iBarrage1, iBarrage2, iBarrage3, iAccuracy, iFlanking1, iFlanking2, iFlanking3, iSentry, iMobility, iNavigation1, iNavigation2, 
iLeader, iLeadership, iTactics, iMorale, iFeintAttack, iEncirclement, iGreekFire, iDesertAdaptation, iBlessed, iRaider, 
iMercenary) = range(iNumPromotions)

# TERRAINS

iNumTerrains = 11
(iGrassland, iPlains, iSemidesert, iDesert, iWetland, iTundra, iIce, iSaltLake, iCoast, iSea, iOcean) = range(iNumTerrains)

# TECHS

iNumTechs = 77
(iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, iShipbuilding, #7
iEvangelism, iMarksmanship, iVassalage, iCurrency, iBotany, iMachinery, #6
iLiterature, iCasteSystem, iCashCropping, iWaterManagement, iAstrolabe, #5
iReligiousPhilosophy, iMosaicArt, iHorsemanship, iLongDistanceTrade, iTextileArts, iSteel, #6
iEducation, iReligiousUnity, iReligiousArchitecture, iChequeSystem, iAgriculturalScience, iEngineering, #6
iAlgebra, iSelectiveBreeding, iCropRotation, iPaper, iCastleBuilding, #5
iMusicTheory, iMedicine, iLevyArmies, iGuilds, iCartography, iAsymmetricWarfare, iSternRudder, #7
iCivilService, iFineryForge, iOptics, #3
iWelfareState, iAlchemy, iCavalryTactics, iMarketEconomy, iAutomata, #5
iPatronage, iChemistry, iCompanies, iBanking, iBlastFurnace, iAstronomy, #6
iCityPlanning, iBlackPowder, iMovableType, iMilitaryDrill, #4
iMetallurgy, iMatchlock, iAdministrativeReforms, #3
iArchitecture, iNavalCannon, iHeavyArmor, iCompass, #4
iWheellock, iProfessionalArmies, iSyncretism, iNavigation, #4
iNavalOrdnance, iFlintlock, iImperialism, iMilitaryScience, #4
iFutureTech, iIslamTech) = range(iNumTechs) #2

# STARTING TECHS

lStartingTechs = [
	# Byzantium 16
	[iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, iShipbuilding, 
		iEvangelism, iMarksmanship, iVassalage, iCurrency, iMachinery, 
		iLiterature, iWaterManagement, iAstrolabe, 
		iHorsemanship, ], 
	 # Makuria 9
	[iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, 
		iEvangelism, iMarksmanship, iVassalage, ],
	# Abbasids 17
	[iIslamTech, iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, iShipbuilding, 
		iEvangelism, iMarksmanship, iVassalage, iCurrency, iBotany, iMachinery, 
		iLiterature, iWaterManagement, iReligiousPhilosophy, 
		iHorsemanship, ], 
	# Chauhan 12
	[iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, 
		iEvangelism, iMarksmanship, iVassalage, iCurrency, iCasteSystem, 
		iHorsemanship, ], 
	# Malwa 12
	[iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, 
		iEvangelism, iMarksmanship, iVassalage, iCurrency, iCasteSystem, 
		iHorsemanship, ], 
	# Samanids 14
	[iIslamTech, iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, 
		iEvangelism, iMarksmanship, iVassalage, iCurrency, iMachinery,
		iLiterature, iWaterManagement, 
		iHorsemanship, ], 
	# Armenia 14
	[iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, iShipbuilding, 
		iEvangelism, iMarksmanship, iVassalage, iCurrency, iMachinery, 
		iLiterature, iHorsemanship, ], 
	# Yemen 16
	[iIslamTech, iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, iShipbuilding, 
		iEvangelism, iMarksmanship, iVassalage, iCurrency, iBotany, iMachinery, 
		iWaterManagement, iAstrolabe, iReligiousPhilosophy, ], 
	# Buyids 18
	[iIslamTech, iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, 
		iEvangelism, iMarksmanship, iVassalage, iCurrency, iBotany, iMachinery,
		iLiterature, iWaterManagement, iReligiousPhilosophy, 
		iHorsemanship, iTextileArts, iSteel, ],
	# Gujarat 19
	[iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, iShipbuilding, 
		iEvangelism, iMarksmanship, iVassalage, iCurrency, iBotany, iMachinery, 
		iLiterature, iCasteSystem, iWaterManagement, 
		iHorsemanship, iTextileArts, iSteel, ], 
	# Ghaznavids 21
	[iIslamTech, iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, iShipbuilding, 
		iEvangelism, iMarksmanship, iVassalage, iCurrency, iMachinery, 
		iLiterature, iWaterManagement, 
		iReligiousPhilosophy, iMosaicArt, iHorsemanship, iLongDistanceTrade, iTextileArts, iSteel,
		iSelectiveBreeding, ],
	# Fatimids 21
	[iIslamTech, iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, iShipbuilding, 
		iEvangelism, iMarksmanship, iVassalage, iCurrency, iBotany, iMachinery, 
		iLiterature, iCashCropping, iWaterManagement, iAstrolabe, 
		iReligiousPhilosophy, iHorsemanship, iLongDistanceTrade, iTextileArts, ], 
	# Georgia 22
	[iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, iShipbuilding, 
		iEvangelism, iMarksmanship, iVassalage, iCurrency, iBotany, iMachinery, 
		iLiterature, iCashCropping, iWaterManagement, iAstrolabe, 
		iReligiousPhilosophy, iMosaicArt, iHorsemanship, iTextileArts, iSteel, ], 
	# Sindh 24
	[iIslamTech, iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, iShipbuilding, 
		iEvangelism, iMarksmanship, iVassalage, iCurrency, iBotany, iMachinery, 
		iLiterature, iCasteSystem, iCashCropping, iWaterManagement, iAstrolabe, 
		iReligiousPhilosophy, iMosaicArt, iHorsemanship, iLongDistanceTrade, iTextileArts, iSteel, ],
	# Seljuks 23
	[iIslamTech, iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, iShipbuilding, 
		iEvangelism, iMarksmanship, iVassalage, iCurrency, iBotany, iMachinery, 
		iLiterature, iWaterManagement, 
		iReligiousPhilosophy, iMosaicArt, iHorsemanship, iLongDistanceTrade, iTextileArts, iSteel,
		iSelectiveBreeding, iEngineering, ],
	# Rum 24
	[iIslamTech, iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, iShipbuilding, 
		iEvangelism, iMarksmanship, iVassalage, iCurrency, iBotany, iMachinery, 
		iLiterature, iWaterManagement, iAstrolabe, 
		iReligiousPhilosophy, iMosaicArt, iHorsemanship, iLongDistanceTrade, iTextileArts, iSteel, 
		iSelectiveBreeding, iEngineering, ],
	# Khwarezm 25
	[iIslamTech, iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, iShipbuilding, 
		iEvangelism, iMarksmanship, iVassalage, iCurrency, iBotany, iMachinery, 
		iLiterature, iCashCropping, iWaterManagement, iAstrolabe, 
		iReligiousPhilosophy, iMosaicArt, iHorsemanship, iLongDistanceTrade, iTextileArts, iSteel, 
		iSelectiveBreeding, iEngineering, ],
	# Antioch 28
	[iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, iShipbuilding, 
		iEvangelism, iMarksmanship, iVassalage, iCurrency, iBotany, iMachinery, 
		iLiterature, iCashCropping, iWaterManagement, iAstrolabe, 
		iReligiousPhilosophy, iHorsemanship, iLongDistanceTrade, iSteel,
		iReligiousUnity, iReligiousArchitecture, iAgriculturalScience, iEngineering,
		iSelectiveBreeding, iCropRotation, iCastleBuilding, ],
	# Crusaders 28
	[iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, iShipbuilding, 
		iEvangelism, iMarksmanship, iVassalage, iCurrency, iBotany, iMachinery, 
		iLiterature, iCashCropping, iWaterManagement, iAstrolabe, 
		iReligiousPhilosophy, iHorsemanship, iLongDistanceTrade, iSteel,
		iReligiousUnity, iReligiousArchitecture, iAgriculturalScience, iEngineering,
		iSelectiveBreeding, iCropRotation, iCastleBuilding, ],
	# Zengids 28
	[iIslamTech, iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, iShipbuilding, 
		iEvangelism, iMarksmanship, iVassalage, iCurrency, iBotany, iMachinery, 
		iLiterature, iWaterManagement, iAstrolabe, 
		iReligiousPhilosophy, iMosaicArt, iHorsemanship, iLongDistanceTrade, iTextileArts, iSteel, 
		iSelectiveBreeding, iEngineering, ],
	# Ghorids 26
	[iIslamTech, iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, iShipbuilding, 
		iEvangelism, iMarksmanship, iVassalage, iCurrency, iBotany, iMachinery, 
		iLiterature, iCashCropping, iWaterManagement, iAstrolabe, 
		iReligiousPhilosophy, iMosaicArt, iHorsemanship, iLongDistanceTrade, iTextileArts, iSteel,
		iReligiousUnity, iAgriculturalScience, iEngineering, ],
	# Oman 26
	[iIslamTech, iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, iShipbuilding, 
		iEvangelism, iMarksmanship, iVassalage, iCurrency, iBotany, iMachinery, 
		iLiterature, iCashCropping, iWaterManagement, iAstrolabe, 
		iReligiousPhilosophy, iMosaicArt, iHorsemanship, iLongDistanceTrade, iTextileArts, iSteel,
		iReligiousUnity, iAgriculturalScience, iEngineering, ],
	# Ayyubids 35
	[iIslamTech, iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, iShipbuilding, 
		iEvangelism, iMarksmanship, iVassalage, iCurrency, iBotany, iMachinery, 
		iLiterature, iCasteSystem, iCashCropping, iWaterManagement, iAstrolabe, 
		iReligiousPhilosophy, iMosaicArt, iHorsemanship, iLongDistanceTrade, iTextileArts, iSteel,
		iEducation, iReligiousUnity, iReligiousArchitecture, iAgriculturalScience, iEngineering, 
		iSelectiveBreeding, iPaper, iCastleBuilding, 
		iMedicine, iGuilds, iSternRudder, ],
	# Mamluks 40
	[iIslamTech, iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, iShipbuilding, 
		iEvangelism, iMarksmanship, iVassalage, iCurrency, iBotany, iMachinery, 
		iLiterature, iCasteSystem, iCashCropping, iWaterManagement, iAstrolabe, 
		iReligiousPhilosophy, iMosaicArt, iHorsemanship, iLongDistanceTrade, iTextileArts, iSteel,
		iEducation, iReligiousUnity, iReligiousArchitecture, iAgriculturalScience, iEngineering,
		iSelectiveBreeding, iCropRotation, iPaper, iCastleBuilding, 
		iMedicine, iGuilds, iCartography, iSternRudder, 
		iFineryForge, 
		iAlchemy, iCavalryTactics, ],
	# Ottomans 45
	[iIslamTech, iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, iShipbuilding, 
		iEvangelism, iMarksmanship, iVassalage, iCurrency, iBotany, iMachinery, 
		iLiterature, iCasteSystem, iCashCropping, iWaterManagement, iAstrolabe, 
		iReligiousPhilosophy, iMosaicArt, iHorsemanship, iLongDistanceTrade, iTextileArts, iSteel,
		iEducation, iReligiousUnity, iReligiousArchitecture, iChequeSystem, iAgriculturalScience, iEngineering,
		iAlgebra, iSelectiveBreeding, iCropRotation, iPaper, iCastleBuilding, 
		iMusicTheory, iMedicine, iLevyArmies, iGuilds, iCartography, iSternRudder, 
		iCivilService, iFineryForge, 
		iAlchemy, iCavalryTactics, ], 
	# Bahmanids 42
	[iIslamTech, iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, iShipbuilding, 
		iEvangelism, iMarksmanship, iVassalage, iCurrency, iBotany, iMachinery, 
		iLiterature, iCasteSystem, iCashCropping, iWaterManagement, iAstrolabe, 
		iReligiousPhilosophy, iMosaicArt, iHorsemanship, iLongDistanceTrade, iTextileArts, iSteel,
		iEducation, iReligiousUnity, iReligiousArchitecture, iAgriculturalScience, iEngineering,
		iAlgebra, iSelectiveBreeding, iCropRotation, iPaper, iCastleBuilding, 
		iMedicine, iLevyArmies, iGuilds, iSternRudder, 
		iCivilService, 
		iAlchemy, iCavalryTactics, ], 
	# Timurids 44
	[iIslamTech, iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, iShipbuilding, 
		iEvangelism, iMarksmanship, iVassalage, iCurrency, iBotany, iMachinery, 
		iLiterature, iCasteSystem, iCashCropping, iWaterManagement, iAstrolabe, 
		iReligiousPhilosophy, iMosaicArt, iHorsemanship, iLongDistanceTrade, iTextileArts, iSteel,
		iEducation, iReligiousUnity, iReligiousArchitecture, iAgriculturalScience, iEngineering,
		iAlgebra, iSelectiveBreeding, iCropRotation, iPaper, iCastleBuilding, 
		iMedicine, iLevyArmies, iGuilds, iCartography, 
		iCivilService, iFineryForge, iOptics, 
		iAlchemy, iCavalryTactics, ], 
	# Ak Koyunlu 40
	[iIslamTech, iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, iShipbuilding, 
		iEvangelism, iMarksmanship, iVassalage, iCurrency, iBotany, iMachinery, 
		iLiterature, iCasteSystem, iCashCropping, iWaterManagement, iAstrolabe, 
		iReligiousPhilosophy, iMosaicArt, iHorsemanship, iLongDistanceTrade, iTextileArts, iSteel,
		iEducation, iReligiousUnity, iAgriculturalScience, iEngineering,
		iSelectiveBreeding, iCropRotation, iPaper, iCastleBuilding, 
		iMusicTheory, iMedicine, iLevyArmies, iGuilds, 
		iCivilService, iFineryForge, 
		iAlchemy, iCavalryTactics, ], 
	# Safavids 51
	[iIslamTech, iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, iShipbuilding, 
		iEvangelism, iMarksmanship, iVassalage, iCurrency, iBotany, iMachinery, 
		iLiterature, iCasteSystem, iCashCropping, iWaterManagement, iAstrolabe, 
		iReligiousPhilosophy, iMosaicArt, iHorsemanship, iLongDistanceTrade, iTextileArts, iSteel,
		iEducation, iReligiousUnity, iReligiousArchitecture, iChequeSystem, iAgriculturalScience, iEngineering, 
		iAlgebra, iSelectiveBreeding, iCropRotation, iPaper, iCastleBuilding,
		iMusicTheory, iMedicine, iLevyArmies, iGuilds, iCartography, iAsymmetricWarfare, iSternRudder, 
		iCivilService, iFineryForge, iOptics, 
		iAlchemy, iCavalryTactics, iMarketEconomy, iAutomata, 
		iBlastFurnace, iPatronage, ],
	# Portugal 51
	[iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, iShipbuilding, 
		iEvangelism, iMarksmanship, iVassalage, iCurrency, iBotany, iMachinery, 
		iLiterature, iCasteSystem, iCashCropping, iWaterManagement, iAstrolabe, 
		iReligiousPhilosophy, iMosaicArt, iHorsemanship, iLongDistanceTrade, iTextileArts, iSteel, 
		iEducation, iReligiousUnity, iReligiousArchitecture, iChequeSystem, iAgriculturalScience, iEngineering, 
		iAlgebra, iSelectiveBreeding, iCropRotation, iPaper, iCastleBuilding, 
		iMusicTheory, iMedicine, iLevyArmies, iGuilds, iCartography, iAsymmetricWarfare, iSternRudder, 
		iCivilService, iFineryForge, iOptics, 
		iAlchemy, iCompanies, iAstronomy, iAutomata, 
		iBlackPowder, iMatchlock, iCompass, ],
	# Mughals 51
	[iIslamTech, iTheology, iOrganizedArmies, iStirrup, iBarter, iHeavyPlough, iMasonry, iShipbuilding, 
		iEvangelism, iMarksmanship, iVassalage, iCurrency, iBotany, iMachinery, 
		iLiterature, iCasteSystem, iCashCropping, iWaterManagement, iAstrolabe, 
		iReligiousPhilosophy, iMosaicArt, iHorsemanship, iLongDistanceTrade, iTextileArts, iSteel, 
		iEducation, iReligiousUnity, iReligiousArchitecture, iChequeSystem, iAgriculturalScience, iEngineering, 
		iAlgebra, iSelectiveBreeding, iCropRotation, iPaper, iCastleBuilding,
		iMusicTheory, iMedicine, iLevyArmies, iGuilds, iCartography, iSternRudder, 
		iCivilService, iFineryForge, iOptics, 
		iAlchemy, iCavalryTactics, iAutomata, 
		iBlastFurnace, iPatronage, iBlackPowder, 
		iCityPlanning ],
 ]

# UNITS

iNumUnits = 205
(iSettler, 
iWorker, 
iSpy, 
iAssassin,
iCaravan, 
iInquisitor, 
iSufiMissionary, 
iHinduMissionary, 
iCatholicMissionary, 
iOrthodoxMissionary, 
iSunniMissionary, 
iShiaMissionary, 
iJavelinman, 
iJavelinman_Caucasian, 
iJavelinman_Turkish, 
iJavelinman_African,
iJavelinman_Indian,
iDaylamiTribesman, 
iAxeman, 
iAxeman_Persian, 
iAxeman_Kurdish,
iAxeman_Caucasian, 
iAxeman_Paulician, 
iGhazi, 
iVarangianGuard, 
iSwordsman, 
iSwordsman_Persian,
iSwordsman_Arab,
iSwordsman_Kipchak,
iSwordsman_Caucasian,
iSwordsman_Indian,
iKshatriya, 
iVishapInfantry, 
iDaylamiInfantry, 
iZanjiSwordsman, 
iPashtunWarrior, 
iManAtArms, 
iMaceman_Harafisha,
iMaceman_Turkish,
iItalianMaceman, 
iFidai, 
iHospitallerSergeant, 
iHospitallerCanon, 
iHospitallerKnight, 
iGhulamGuard, 
iHeavySwordsman, 
iHeavySwordsman_Generic, 
iHeavySwordsman_Rajput, 
iHeavySwordsman_Afghan, 
iMujahid, 
iAfghanInfantry, 
iMarathaWarrior,
iSpearman, 
iSpearman_Turkish, 
iSpearman_African, 
iSpearman_Caucasian, 
iSpearman_Harafisha, 
iSpearman_Bedouin,
iSpearman_Indian, 
iPeasant, 
iAbnaSpearman, 
iKhorasaniSpearman, 
iZanjiSpearman, 
iHeavySpearman, 
iHeavySpearman_Arab, 
iHeavySpearman_Indian, 
iHeavySpearman_Kipchak, 
iPikeman, 
iAfghanPikeman, 
iArquebusier, 
iArquebusier_African, 
iArquebusier_Indian, 
iArquebusier_Bedouin, 
iMusketman, 
iMusketman_Indian, 
iMusketman_Bedouin, 
iGrenadier, 
iArcher, 
iArcher_Persian,
iArcher_Turkish,
iArcher_African,
iArcher_Caucasian,
iArcher_Bedouin,
iArcher_Arab,
iArcher_Syrian,
iArcher_Indian,
iDihqanArcher, 
iKshatriyaArcher, 
iMarksman, 
iMarksman_Arab, 
iMarksman_Turkish, 
iMarksman_Indian, 
iMarksman_Bedouin,
iMarksman_Caucasian, 
iLongbowman, 
iNaffatun, 
iMarine, 
iItalianCrossbowman, 
iGreekFlamethrower, 
iSkirmisher, 
iSkirmisher_Arab, 
iBulgarianRaider, 
iHorseman, 
iHorseman_Persian, 
iHorseman_Bedouin, 
iHorseman_Indian, 
iBerberCavalry, 
iHorseArcher, 
iHorseArcher_Turkish, 
iHorseArcher_Kipchak, 
iHorseArcher_Christian, 
iHorseArcher_Indian, 
iGhulamHorseArcher, 
iSeljukHorseArcher, 
iRajputCavalry, 
iCamelArcher, 
iMountedInfantry, 
iMountedInfantry_Persian, 
iArabianSheikh, 
iPashtunCavalry, 
iMarathaCavalry, 
iHeavyHorseArcher, 
iHeavyHorseArcher_Turkish,
iMongolHorseArcher, 
iQizilbash, 
iLancer, 
iLancer_Turkish, 
iLancer_Syrian, 
iLancer_Frankish, 
iLancer_Kipchak,
iTawashiLancer, 
iNormanKnight, 
iKhwarezmianLancer, 
iCataphract, 
iMonaspaLancer, 
iJagirdar, 
iKnightOfJerusalem, 
iCamelRider, 
iBedouinCamelRider, 
iGhulamLancer, 
iTemplarSergeant,  
iTemplarKnight, 
iHeavyLancer, 
iHeavyLancer_Mamluk, 
iHeavyLancer_Frankish, 
iHeavyLancer_Indian, 
iMamluk, 
iTurkomanRaider, 
iHeavyCavalry, 
iLightCavalry, 
iLightCavalry_Bedouin,
iCamelGunner, 
iCamelGunner_Indian, 
iWarElephant, 
iHeavyWarElephant, 
iCatapult, 
iTrebuchet, 
iSiegeEngineer, 
iBombard, 
iGreatBombard, 
iCannon, 
iSiegeElephant, 
iWorkBoat, 
iGalley, 
iDhow, 
iWarGalley, 
iGreatGalley, 
iRoundship, 
iBaghlah, 
iLanternas, 
iCaravel, 
iCarrack, 
iGalleon, 
iFrigate, 
iGreatProphet, 
iGreatProphet2, 
iGreatProphet3, 
iGreatArist, 
iGreatArtist2, 
iGreatScholar, 
iGreatScholar2, 
iGreatMerchant, 
iGreatMerchant2, 
iGreatEngineer, 
iGreatGeneral, 
iGreatGeneral2, 
iGreatGeneral3, 
iGreatGeneral4, 
iGreatGeneral5, 
iGreatSpy,
iRelic1,
iRelic2,
iRelic3,
iRelic4,
iRelic5,
iRelic6,
iRelic7,
iRelic8,
iRelic9,
iRelic10,
iRelic11,
iRelic12,
iIqtadar,
iDakhani,
iVlastela) = range(iNumUnits)

# RESOURCES

iNumResources = 41
(iHorse, iIron, iCopper, iSulfur, iMarble, iStone, iClam, iCrab, iCow, iDeer, iFish, iPig, iRice, iSheep, iWheat, iBarley, 
iDye, iFur, iGold, iIncense, iSilk, iSilver, iSpices, iSugar, iWine, iWhale, iHemp, iCotton, iHoney, iSalt, iOlives, 
iCitrus, iApples, iDates, iGems, iPearls, iIvory, iOpium, iCoffee, iSorghum, iOil) = range(iNumResources)

# IMPROVEMENTS

iFarm = 4
iMine = 6
iWorkshop = 7
iWindmill = 8
iWatermill = 9
iCottage = 19
iHamlet = 20
iVillage = 21
iTown = 22
iFort = 23

# BUILDINGS

iNumBuildings = 147
(iPalace, iForbiddenPalace, iWalls, iTowerHouse, iCastle, iQalat, iBarracks, iSlaveBarracks, iArcheryRange, iBowyer, 
iStable, iHorseBreeder, iGranary, iAqueduct, iStepwell, iPublicBaths, iHammam, iHospital, iBimaristan, iLighthouse, 
iTradingPost, iHarbor, iKarimiFunduq, iVenetianQuarter, iGenoeseQuarter, iFeitoria, iSufiShrine, iDrydock, iBlacksmith, 
iMint, iWeaponsmith, iGuildHall, iCraftsmensQuarter, iFoundry, iMonument, iNormanChapel, iKhachkar, iAlchemistsLab, iLibrary, 
iSanskritCollege, iObservatory, iUniversity, iNizamiyya, iFairground, iSouk, iYam, iRacingTrack, iHippodrome, 
iPotteryWorkshop, iIkonersStudio, iMarket, iSlaveMarket, iButcher, iConfectioner, iBank, iTanner, iWeaver, iSilkWeaver, 
iTextileMill, iCourthouse, iDivan, iChancery, iInn, iHan, iCaravanserai, iBrothel, iDungeon, iMausoleum, iJewishQuarter, 
iCatholicTemple, iCatholicCathedral, iCatholicMonastery, iCatholicShrine, iOrthodoxTemple, iOrthodoxCathedral, 
iOrthodoxMonastery, iOrthodoxShrine, iBuddhistMonastery, iHinduTemple, iHinduCathedral, iHinduMonastery, iHinduShrine, 
iSunniTemple, iSunniCathedral, iSunniMonastery, iSunniShrine, iShiaTemple, iShiaCathedral, iShiaMonastery, iShiaShrine, 
iPlague, iHeroicEpic, iNationalEpic, iMilitaryAcademy, iOxfordUniversity, iRoyalTomb, iRoyalMint, iMedicalSchool, iDenOfSpies, 
iGreatLighthouse, iTheodosianWalls, iGreatObservatory, iKrakDesChevaliers, iAlAzhar, iDomeOfTheRock, iInventorsWorkshop, 
iGrandBazaar, iShalimarGardens, iTopkapiPalace, iSpiralMinaret, iHouseOfWisdom, iTombOfKhalid, iShahnameh, iMinaretOfJam, 
iQutbMinar, iTajMahal, iTowerOfVictory, iBlueMosque, iMevlanasTomb, iShahMosque, iKizilKule, iKutlugTimur, iRaniKiVav, 
iBagratiCathedral, iSoltaniyeh, iRedFort, iBamyanBuddha, iNarekavank, iProphetsMosque, iIbnBattuta, iImamRezaShrine, iBridge33, 
iImageOfEdessa, iTrueCross, iHolyLance, iCrownOfThorns, iBonesOfTheMagi, iHeadOfJohnTheBaptist, iCloakOfTheProphet, 
iSacredSeal, iHolyBanner, iBlessedMantle, iBeardOfMuhammad, iSwordOfAli, iBagh, iNoria, iMarineAcademy) = range(iNumBuildings)

# REGIONS (PROVINCES) for RFC RiseAndFall, RFC Stability, RFC AIWars, MEM Religions and MEM Regional Recruitment

iNumRegions = 131
(rNoRegion, rBlackSea, rMediterraneanSea, rRedSea, rPersianGulf, rCaspianSea, rAralSea, rArabianSea, rThrace, rBulgaria,
rAsia, rBithynia, rLycia, rPontus, rGalatia, rPaphlagonia, rCilicia, rCappadocia, rLesserArmenia, rRhodes,
rCyprus, rLowerEgypt, rUpperEgypt, rSinai, rNobatia, rMakuria, rAlodia, rAksum, rMerebMellash, rYemen, 
rOman, rBahrain, rMahra, rSuqutra, rHadhramaut, rHejaz, rArabia, rSahara, rKhuzestan, rMesopotamia,
rVaspurakan, rGreaterArmenia, rKars, rGeorgia, rShirvan, rAzerbaijan, rNorthernCaucasus, rPalestine, rJordan, rSyria,
rNorthernSyria, rTrebizond, rFars, rKerman, rHormuz, rLuristan, rKurdistan, rDashteKavir, rDashteLut, rYazd,
rHindukush, rWesternKhorasan, rKhwarezm, rSogd, rKyzylKum, rBactria, rSistan, rBalochistan, rSindh, rJazira,
rMakran, rGujarat, rFarghana, rPunjab, rGhazni, rGandhar, rKandahar, rEdessa, rMaharashtra, rKarnataka,
rMalwa, rRajputana, rUttarBharat, rGird, rDuggar, rHimalaya, rKaraKum, rJibal, rMazandaran, rPamir,
rTienShan, rTaklaMakan, rAsuristan, rGoa, rEasternKhorasan, rLakeVan, rLakeUrmia, rDeadSea, rLakeSevan,
rSeaOfGalilee, rNamakLake, rLakeTuz, rLakeEgirdir, rPushkarLake, rBadaTalaab, rLakeTharthar, rLakeRazazah, 
rLakeHamun, rLakeMoeris, rSeaOfMarmara, rLebanon, rConstantinople, Thessaly, rCentralGreece, rMorea, rLibya, rSerbia, rEpirus, rCrete, rCephalonia, rDagestan,
rKrim, rSarygamyshLake, rKyzylorda, rSkadarLake, rGarabogazkol, rMacedonia, rProkletije, rCarpathians, rKalmykia, rCircassia) = range(iNumRegions)

# Region lists: replacement for RFC TL/BR stability areas and AI war maps

# Core (spawn) regions = RFC tCoreAreasTL/BR and AIWars +10
lCoreRegions = [
	[rThrace, rAsia], # Byzantium
	[rMakuria], # Makuria
	[rMesopotamia, rSyria], # Abbasids
	[rRajputana], # Chauhan
	[rMalwa], # Malwa
	[rBactria, rSogd, rEasternKhorasan], # Samanids
	[rGreaterArmenia], # Armenia
	[rYemen], # Yemen
	[rFars, rLuristan], # Buyids
	[rGujarat], # Gujarat
	[rGhazni, rKandahar], # Ghaznavids
	[rLowerEgypt], # Fatimids
	[rGeorgia], # Georgia
	[rSindh], # Sindh
	[rJibal, rLuristan, rKurdistan, rWesternKhorasan, rEasternKhorasan], # Seljuks
	[rCappadocia, rGalatia], # Rum
	[rKhwarezm, rSogd, rKyzylorda], # Khwarezm
	[rNorthernSyria, rEdessa], # Antioch
	[rPalestine], # Crusaders
	[rAsuristan, rJazira], # Zengids
	[rGandhar, rHindukush], # Ghorids
	[rOman, rHormuz, rMahra], # Oman
	[rLowerEgypt, rSinai, rJordan, rSyria], # Ayyubids
	[rLowerEgypt, rUpperEgypt, rSinai], # Mamluks
	[rBithynia, rAsia], # Ottomans
	[rKarnataka, rMaharashtra], # Bahmanids
	[rSogd, rFarghana, rBactria], # Timurids
	[rAsuristan, rJazira, rAzerbaijan], # Ak Koyunlu
	[rAzerbaijan, rShirvan, rKurdistan, rMazandaran], # Safavids
	[rGoa], # Portugal
	[rPunjab, rUttarBharat, rGandhar], # Mughals
]

lRespawnRegions = [
	[rThrace, rAsia], # Byzantium
	[rMakuria], # Makuria
	[rMesopotamia], # Abbasids ***** (Smaller core)
	[rRajputana], # Chauhan
	[rMalwa], # Malwa
	[rBactria, rEasternKhorasan], # Samanids ***** (Smaller core)
	[rCilicia], # Armenia ***** (Cilicia)
	[rYemen], # Yemen
	[rFars, rLuristan], # Buyids
	[rGujarat], # Gujarat
	[rGhazni, rKandahar], # Ghaznavids
	[rLowerEgypt], # Fatimids
	[rGeorgia], # Georgia
	[rSindh], # Sindh
	[rJibal, rLuristan, rKurdistan, rWesternKhorasan, rEasternKhorasan], # Seljuks
	[rCappadocia], # Rum ***** (Karaman)
	[rKhwarezm, rSogd, rKyzylorda], # Khwarezm
	[rNorthernSyria], # Antioch
	[rCyprus], # Crusaders ***** (Cyprus)
	[rAsuristan, rJazira], # Zengids
	[rUttarBharat, rPunjab, rDuggar], # Ghorids ***** (Delhi Sultanate)
	[rOman, rHormuz, rMahra], # Oman
	[rLowerEgypt, rSinai, rJordan, rSyria], # Ayyubids
	[rLowerEgypt, rUpperEgypt, rSinai, rJordan], # Mamluks
	[rBithynia, rAsia, rGalatia], # Ottomans ***** (Larger core)
	[rKarnataka, rMaharashtra], # Bahmanids
	[rSogd, rFarghana, rBactria], # Timurids
	[rAsuristan, rJazira, rAzerbaijan], # Ak Koyunlu
	[rAzerbaijan, rShirvan, rKurdistan, rMazandaran], # Safavids
	[rGoa], # Portugal
	[rUttarBharat, rGandhar, rPunjab], # Mughals
]

# Normal regions = RFC tNormalAreasTL/BR and AIWars +5
lNormalRegions = [
	[rPontus, rPaphlagonia, rBithynia, rTrebizond, rEpirus, Thessaly, rCentralGreece, rMorea, rCrete, rCephalonia, rKrim, rProkletije, rMacedonia], # Byzantium
	[rNobatia, rAlodia], # Makuria
	[rNorthernSyria, rPalestine, rAsuristan, rJazira], # Abbasids
	[rMalwa, rUttarBharat, rGird], # Chauhan
	[], # Malwa
	[rWesternKhorasan, rSistan], # Samanids
	[rVaspurakan, rKars, rLesserArmenia], # Armenia
	[rHadhramaut], # Yemen
	[rYazd, rJibal, rKerman, rKurdistan, rKhuzestan], # Buyids
	[rMaharashtra], # Gujarat
	[rGandhar, rPunjab, rEasternKhorasan], # Ghaznavids
	[rUpperEgypt, rSinai, rPalestine], # Fatimids
	[rShirvan], # Georgia
	[rPunjab], # Sindh
	[rFars, rYazd], # Seljuks
	[rPontus, rLesserArmenia], # Rum
	[rWesternKhorasan, rEasternKhorasan, rBactria, rKyzylKum], # Khwarezm
	[rCilicia, rLebanon, rCyprus], # Antioch
	[rJordan, rCyprus, rLebanon, rNorthernSyria], # Crusaders
	[rSyria, rEdessa], # Zengids
	[rPunjab, rGhazni, rKandahar], # Ghorids
	[rMakran, rBahrain], # Oman
	[rUpperEgypt, rPalestine, rLebanon, rNorthernSyria, rHejaz, rLibya], # Ayyubids
	[rPalestine, rJordan, rSyria], # Mamluks
	[rThrace, rCappadocia, rLycia, rGalatia, rPaphlagonia, rPontus, rLesserArmenia, rCilicia], # Ottomans
	[], # Bahmanids
	[rKhwarezm, rWesternKhorasan, rEasternKhorasan, rTaklaMakan, rMazandaran, rKyzylorda], # Timurids
	[rVaspurakan], # Ak Koyunlu
	[rLuristan, rJibal, rFars, rWesternKhorasan, rEasternKhorasan, rYazd, rKerman, rKhuzestan], # Safavids
	[rMaharashtra, rOman, rHormuz, rMakran], # Portugal
	[rGird, rGujarat, rSindh, rMalwa, rRajputana], # Mughals
]

# Lists of regions that will flip on resurrection if owned by a minor civ or barbarians
lRespawnNormalRegions = [
	[rPontus, rPaphlagonia, rTrebizond, rBithynia, rRhodes, rCyprus, rEpirus, Thessaly, rCentralGreece, rMorea, rCrete], # Byzantium ******
	[rNobatia, rAlodia], # Makuria
	[rAsuristan, rKhuzestan], # Abbasids ******
	[], # Chauhan *****
	[], # Malwa
	[rWesternKhorasan, rSogd, rSistan], # Samanids
	[], # Armenia *****
	[rHadhramaut], # Yemen
	[rYazd, rJibal, rKerman, rKurdistan, rKhuzestan], # Buyids
	[rMaharashtra], # Gujarat
	[rGandhar, rPunjab, rEasternKhorasan], # Ghaznavids
	[rUpperEgypt, rSinai, rPalestine], # Fatimids
	[rShirvan], # Georgia
	[rPunjab], # Sindh
	[rFars, rYazd, rWesternKhorasan, rEasternKhorasan], # Seljuks
	[rCilicia], # Rum *****
	[rWesternKhorasan, rEasternKhorasan, rBactria, rKyzylKum, rKyzylorda], # Khwarezm
	[rCilicia, rLebanon, rJazira, rCyprus], # Antioch
	[rRhodes], # Crusaders *****
	[rSyria], # Zengids
	[rGird, rSindh, rRajputana], # Ghorids ***** (Delhi)
	[rMakran, rBahrain], # Oman
	[rUpperEgypt, rPalestine, rLebanon, rNorthernSyria, rHejaz], # Ayyubids
	[rSinai, rJordan, rPalestine], # Mamluks
	[rCappadocia, rLycia, rPaphlagonia, rPontus, rLesserArmenia, rCilicia, rThrace], # Ottomans *****
	[], # Bahmanids
	[rKhwarezm, rBactria, rWesternKhorasan, rEasternKhorasan, rTaklaMakan, rKyzylorda], # Timurids
	[rVaspurakan], # Ak Koyunlu
	[rLuristan, rJibal, rFars, rWesternKhorasan, rEasternKhorasan, rYazd, rKerman, rKhuzestan], # Safavids
	[rKarnataka, rMaharashtra, rOman, rYemen, rMakran, rHormuz], # Portugal
	[rGujarat, rSindh, rMalwa, rRajputana], # Mughals
]

# Broader regions = RFC tBroaderAreasTL/BR and AIWars +2
lBroaderRegions = [
	[rLycia, rCappadocia, rGalatia, rLesserArmenia, rCilicia, rLowerEgypt, rPalestine, rLebanon, rRhodes, rCyprus, rNorthernSyria, rEdessa, rSyria, rJordan, rSinai, rUpperEgypt, rLibya], # Byzantium
	[rAksum, rMerebMellash], # Makuria
	[rKhuzestan, rGreaterArmenia, rShirvan, rAzerbaijan, rWesternKhorasan, rEasternKhorasan, rFars, rJibal, rLuristan, rKurdistan, rBahrain, rHejaz, rYemen, rOman, rEdessa, rLebanon, rDagestan], # Abbasids
	[rGujarat], # Chauhan
	[rRajputana, rGujarat, rGird], # Malwa
	[rFarghana, rBalochistan, rMazandaran], # Samanids
	[rAzerbaijan, rGeorgia, rEdessa, rCilicia, rDagestan], # Armenia
	[rSuqutra], # Yemen
	[rMazandaran, rHormuz, rWesternKhorasan, rOman], # Buyids
	[rMalwa, rRajputana, rUttarBharat], # Gujarat
	[rWesternKhorasan, rSistan, rBalochistan, rHindukush], # Ghaznavids
	[rHejaz, rLebanon], # Fatimids
	[rKars, rTrebizond, rGreaterArmenia, rAzerbaijan, rDagestan, rKalmykia, rNorthernCaucasus, rDagestan], # Georgia
	[rBalochistan, rGujarat], # Sindh
	[rMesopotamia, rAsuristan, rAzerbaijan, rSistan, rKhuzestan, rMazandaran, rKerman], # Seljuks
	[rBithynia, rPaphlagonia, rAsia, rLycia, rCilicia, rThrace, rVaspurakan], # Rum
	[rSistan, rMazandaran, rYazd, rKerman, rFars, rLuristan, rKurdistan, rJibal, rAzerbaijan, rBalochistan], # Khwarezm
	[rSyria, rJordan, rPalestine], # Antioch
	[rLowerEgypt, rSyria, rEdessa, rLibya], # Crusaders
	[rNorthernSyria, rPalestine, rLebanon, rJordan], # Zengids
	[rBalochistan, rDuggar, rUttarBharat, rGird, rSistan, rSindh, rRajputana], # Ghorids
	[rFars], # Oman
	[rNobatia, rMakuria, rYemen, rJazira, rEdessa], # Ayyubids
	[rLebanon, rNorthernSyria, rCilicia, rEdessa, rNobatia, rMakuria], # Mamluks
	[rRhodes, rCyprus, rVaspurakan, rGreaterArmenia, rKars, rSinai, rLowerEgypt, rUpperEgypt, rMesopotamia, rAsuristan, rJazira, rEdessa, rSyria, rLebanon, rNorthernSyria, rPalestine, rJordan, rHejaz, rLibya, rBulgaria,
	rSerbia, rEpirus, Thessaly, rCentralGreece, rMorea, rCrete, rCephalonia, rDagestan], # Ottomans
	[rMalwa, rGujarat, rGoa], # Bahmanids
	[rGandhar, rSistan, rAzerbaijan, rJibal, rLuristan, rKurdistan, rYazd, rFars, rKerman, rPunjab, rMakran, rGeorgia, rShirvan, rGreaterArmenia, rMesopotamia, rKyzylKum, rDagestan], # Timurids
	[rLesserArmenia, rGreaterArmenia, rShirvan, rMesopotamia, rEdessa, rKhuzestan, rLuristan, rKurdistan, rFars, rYazd, rKerman, rMazandaran], # Ak Koyunlu
	[rHormuz, rBalochistan, rSistan, rMesopotamia, rGreaterArmenia, rGeorgia, rDagestan], # Safavids
	[rYemen, rHadhramaut, rMahra, rSuqutra, rBahrain, rGujarat], # Portugal
	[rMaharashtra, rKarnataka, rGandhar, rDuggar, rBalochistan], # Mughals
]

lRespawnBroaderRegions = [
	[rLycia, rCappadocia, rGalatia, rLesserArmenia, rCilicia], # Byzantium ***** 
	[rAksum, rMerebMellash], # Makuria
	[], # Abbasids ***** 
	[rGujarat, rMalwa, rGird], # Chauhan
	[rRajputana, rGujarat, rGird], # Malwa
	[rFarghana, rBalochistan], # Samanids
	[rEdessa, rNorthernSyria, rLesserArmenia], # Armenia ***** 
	[rSuqutra], # Yemen
	[rMazandaran, rHormuz, rWesternKhorasan, rOman], # Buyids
	[rMalwa, rRajputana, rUttarBharat], # Gujarat
	[rWesternKhorasan, rSistan, rBalochistan, rHindukush], # Ghaznavids
	[rHejaz, rLebanon], # Fatimids
	[rKars, rTrebizond, rGreaterArmenia, rAzerbaijan, rKalmykia, rNorthernCaucasus, rDagestan], # Georgia
	[rBalochistan, rGujarat], # Sindh
	[rMesopotamia, rAsuristan, rAzerbaijan, rSistan, rKhuzestan, rMazandaran, rKerman], # Seljuks
	[], # Rum ***** 
	[rSistan, rMazandaran, rYazd, rKerman, rFars, rLuristan, rKurdistan, rJibal, rAzerbaijan, rBalochistan], # Khwarezm
	[rSyria, rJordan, rPalestine], # Antioch
	[rLowerEgypt, rLebanon, rSyria, rEdessa], # Crusaders
	[rLebanon, rNorthernSyria, rPalestine, rJordan], # Zengids
	[rDuggar, rUttarBharat, rSistan, rGandhar], # Ghorids *****
	[rFars], # Oman
	[rNobatia, rMakuria, rYemen, rJazira, rEdessa], # Ayyubids
	[rLebanon, rNorthernSyria, rCilicia, rEdessa, rNobatia, rMakuria], # Mamluks
	[rRhodes, rCyprus, rVaspurakan, rGreaterArmenia, rKars, rSinai, rLowerEgypt, rUpperEgypt, rMesopotamia, rAsuristan, rJazira, rEdessa, rSyria, rLebanon, rNorthernSyria, rPalestine, rJordan, rHejaz], # Ottomans
	[rMalwa, rGujarat, rGoa], # Bahmanids
	[rGandhar, rSistan, rAzerbaijan, rJibal, rLuristan, rKurdistan, rYazd, rFars, rKerman, rPunjab, rMakran, rGeorgia, rShirvan, rGreaterArmenia, rMesopotamia, rKyzylKum, rKyzylorda], # Timurids
	[rLesserArmenia, rGreaterArmenia, rShirvan, rMesopotamia, rEdessa, rKhuzestan, rLuristan, rKurdistan, rFars, rYazd, rKerman, rMazandaran], # Ak Koyunlu
	[rHormuz, rBalochistan, rSistan, rMesopotamia, rGreaterArmenia, rGeorgia], # Safavids
	[rYemen, rHadhramaut, rMahra, rSuqutra, rBahrain], # Portugal
	[rMaharashtra, rKarnataka, rGandhar, rDuggar, rBalochistan], # Mughals
]

lRevealRegions = [
	[rThrace, rAsia, rPontus, rPaphlagonia, rTrebizond, rRhodes, rCilicia, rLesserArmenia, rMediterraneanSea, rBlackSea, rCyprus, rKars, rSyria, rLebanon, rNorthernSyria, rPalestine, rEpirus, rMacedonia, 
	Thessaly, rJordan, rLibya, rLowerEgypt, rSinai, rCephalonia, rKrim, rProkletije], # Byzantium
	[rMakuria, rNobatia, rAlodia], # Makuria
	[rMesopotamia, rSyria, rLebanon, rNorthernSyria, rPalestine, rAsuristan, rJazira], # Abbasids
	[rRajputana], # Chauhan
	[rMalwa], # Malwa
	[rBactria, rSogd], # Samanids
	[rGreaterArmenia, rKars, rVaspurakan], # Armenia
	[rYemen], # Yemen
	[rFars, rYazd, rKerman, rLuristan, rKurdistan, rJibal, rMazandaran, rWesternKhorasan, rKhuzestan, rMesopotamia], # Buyids
	[rGujarat, rMaharashtra], # Gujarat
	[rGhazni, rKandahar, rWesternKhorasan, rEasternKhorasan, rSistan, rBactria], # Ghaznavids
	[rLowerEgypt], # Fatimids
	[rGeorgia], # Georgia
	[rSindh, rPunjab], # Sindh
	[rJibal, rLuristan, rKurdistan, rFars, rYazd, rWesternKhorasan, rEasternKhorasan], # Seljuks
	[rCappadocia, rGalatia, rLesserArmenia], # Rum
	[rKhwarezm, rSogd, rWesternKhorasan, rEasternKhorasan, rBactria, rKyzylorda], # Khwarezm
	[rPalestine, rLebanon, rNorthernSyria, rCyprus, rRhodes, rMediterraneanSea, rCilicia], # Antioch
	[rPalestine, rLebanon, rNorthernSyria, rCyprus, rRhodes, rMediterraneanSea, rCilicia], # Crusaders
	[rAsuristan, rJazira, rMesopotamia, rLebanon, rNorthernSyria, rSyria, rPalestine], # Zengids
	[rGandhar, rHindukush, rGhazni], # Ghorids
	[rOman, rHormuz], # Oman
	[rLowerEgypt, rUpperEgypt, rSinai, rJordan, rSyria, rLebanon, rNorthernSyria], # Ayyubids
	[rLowerEgypt, rUpperEgypt, rSinai, rJordan, rSyria, rLebanon, rNorthernSyria], # Mamluks
	[rBithynia, rThrace, rAsia, rCappadocia, rGalatia, rPontus], # Ottomans
	[rKarnataka, rMaharashtra, rMalwa, rGujarat, rGoa], # Bahmanids
	[rSogd, rFarghana, rWesternKhorasan, rEasternKhorasan, rKhwarezm, rKyzylKum, rKyzylorda], # Timurids
	[rAsuristan, rJazira, rMesopotamia, rLesserArmenia], # Ak Koyunlu
	[rAzerbaijan, rShirvan, rKurdistan, rMazandaran], # Safavids
	[rGoa, rRedSea, rPersianGulf, rArabianSea], # Portugal
	[rUttarBharat, rGird, rPunjab, rGandhar, rDuggar, rRajputana, rMaharashtra, rMalwa, rGujarat, rSindh, rBactria, rHindukush, rGhazni, rKandahar], # Mughals
]

# Cities in these regions like to be independent and in case of secession will declare independence before other cities
# (unless they are in the civ's core area)
lUnrulyRegions = [rSyria, rAsuristan, rKarnataka, rFarghana, rBalochistan, rGandhar, rGreaterArmenia, rNorthernCaucasus, 
rGeorgia, rAksum, rMerebMellash, rYemen, rShirvan, rHadhramaut, rBahrain, rAzerbaijan, rMazandaran, rSuqutra, rRajputana, 
rMalwa, rKarnataka, rTaklaMakan, rDuggar, rMaharashtra, rTrebizond, rEdessa, rBulgaria]

### COMPANIES
	
# Companies will only settle in their preferred regions
lCompanyRegions = [
# Sufi Order
[], #all
# Karimi
[], #all
# Nizari
[rJordan, rPalestine, rLebanon, rNorthernSyria, rSyria, rJazira, rAsuristan, rLuristan, rKurdistan, rJibal, rMazandaran, rAzerbaijan, rFars, rYazd, rKerman, rLowerEgypt],
# Hospitallers
[rSinai, rPalestine, rLebanon, rNorthernSyria, rCilicia, rLycia, rCyprus, rRhodes, rAsia, rJazira],
# Templars
[rSinai, rPalestine, rLebanon, rNorthernSyria, rCyprus, rJordan, rLowerEgypt],
# Venetians
[rLowerEgypt, rSinai, rPalestine, rLebanon, rNorthernSyria, rCilicia, rLycia, rCyprus, rRhodes, rAsia, rThrace, rKrim],
# Genoans
[rLowerEgypt, rSinai, rPalestine, rLebanon, rNorthernSyria, rCilicia, rLycia, rCyprus, rRhodes, rAsia, rThrace, rPaphlagonia, rTrebizond, rGeorgia, rKrim],
# Portuguese
[rMerebMellash, rYemen, rSuqutra, rHadhramaut, rMahra, rOman, rHormuz, rMakran, rSindh, rGujarat, rMaharashtra, rGoa],
# Silk
[rSogd, rWesternKhorasan, rKhwarezm, rFarghana, rKyzylKum, rTaklaMakan, rPamir, rBactria, rEasternKhorasan, rDashteKavir, rDashteLut, rJibal, rMazandaran, rKyzylorda],
# Pisans
[rLowerEgypt, rSinai, rPalestine, rLebanon, rNorthernSyria, rCilicia, rLycia, rCyprus, rRhodes, rAsia, rThrace, rKrim],
# Tamils
[rGird, rSindh, rGujarat, rMaharashtra, rKarnataka, rGoa, rMalwa, rRajputana],
]

### TITLES

# Title eligibility
lTitleRegions = [
# Roman Emperor
[rThrace, rAsia, rLycia, rCappadocia, rPaphlagonia, rPontus, rGalatia, rBithynia, rLesserArmenia, rCilicia, rTrebizond],
# Caliph
[rMesopotamia],
# Shahanshah
[rFars, rKerman, rLuristan, rKurdistan, rYazd, rJibal, rMazandaran, rWesternKhorasan],
# Sharif of Mecca
[rHejaz],
# Protector of the Holy Sepulchre
[rPalestine],
# Raja Vikramaditya
[rUttarBharat, rGird, rDuggar, rPunjab, rSindh, rGujarat, rMaharashtra, rKarnataka, rGoa, rMalwa, rRajputana],
]

### PLAGUE

# Regions that will be hit the hardest
lBlackDeathRegions = [ rThrace, rAsia, rTrebizond, rLycia, rLowerEgypt, rUpperEgypt, rSinai, rPalestine,
rJordan, rSyria, rNorthernSyria, rEdessa, rJazira, rMesopotamia, rAsuristan, rCyprus, rShirvan, rGreaterArmenia,
rLesserArmenia, rGeorgia, rKars, rJibal, rKurdistan, rWesternKhorasan, rEasternKhorasan, rBactria, rKhwarezm, 
rSogd, rTaklaMakan, rKyzylorda]

# Civs that are likely to be spared
lBlackDeathSurvivors = [ iOttomans, iMamluks, iSafavids, iChauhan, iGujarat, iBahmanids, iMughals, iMalwa, iOman, iYemen ]

# Plague is most likely to start within the lands of these civs
lBlackDeathStarters = [ iByzantium, iAbbasids, iSeljuks, iKhwarezm ]

### JEWS

# Jewish migration in Religions.py
jewsEarlyRegions = [ rYemen, rPalestine, rSyria, rLebanon, rNorthernSyria, rJazira, rEdessa, rLowerEgypt, rMesopotamia, rEasternKhorasan, rFars, rGujarat, rMaharashtra ]
jewsMiddleRegions = [ rLycia, rThrace, rBithynia, rAsia, rPontus, rGalatia, rPaphlagonia, rCilicia, rCappadocia, rEasternKhorasan, rFars, rSyria, rLebanon, rNorthernSyria ]
jewsLateRegions = []

### PIETY

# Piety / Favor Levels
iFavorLevel_RoyalSaint = 100
iFavorLevel_Saint = 90
iFavorLevel_Blessed = 80
iFavorLevel_Devoted = 70
iFavorLevel_Righteous = 60
iFavorLevel_Faithful = 50
iFavorLevel_Believer = 40
iFavorLevel_Unreliable = 30
iFavorLevel_Heathen = 20
iFavorLevel_Apostate = 10
iFavorLevel_Heretic = 0

tFavorLevelsBlessing = 			(  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1)
tFavorLevelsHappinessBonus = 	( -2, -1,  0,  0,  0,  0,  0,  1,  1,  2,  2)
tFavorLevelsStabilityBonus = 	( -5, -2,  0,  0,  0,  1,  2,  3,  4,  5,  10)

lFavorLevels = [
	iFavorLevel_Heretic,
	iFavorLevel_Apostate,
	iFavorLevel_Heathen,
	iFavorLevel_Unreliable,
	iFavorLevel_Believer,
	iFavorLevel_Faithful,
	iFavorLevel_Righteous,
	iFavorLevel_Devoted,
	iFavorLevel_Blessed,
	iFavorLevel_Saint,
	iFavorLevel_RoyalSaint,
	]

lFavorLevelsText = [
	"TXT_KEY_FAVOR_LEVEL_HERETIC",
	"TXT_KEY_FAVOR_LEVEL_APOSTATE",
	"TXT_KEY_FAVOR_LEVEL_HEATHEN",
	"TXT_KEY_FAVOR_LEVEL_UNRELIABLE",
	"TXT_KEY_FAVOR_LEVEL_BELIEVER",
	"TXT_KEY_FAVOR_LEVEL_FAITHFUL",
	"TXT_KEY_FAVOR_LEVEL_RIGHTEOUS",
	"TXT_KEY_FAVOR_LEVEL_DEVOTED",
	"TXT_KEY_FAVOR_LEVEL_BLESSED",
	"TXT_KEY_FAVOR_LEVEL_SAINT",
	"TXT_KEY_FAVOR_LEVEL_ROYAL_SAINT",
	]

lHolyWarTypes = [
	"TXT_KEY_HOLY_WAR_HOLY_CITY",
	"TXT_KEY_HOLY_WAR_INFIDEL",
	"TXT_KEY_HOLY_WAR_HERETIC",
	]

# RELICS

# Relic dictionary { relicID : unitID, regionList }
relics = {
	iImageOfEdessa			: (iRelic1, [rThrace, rEdessa, rEdessa, rCilicia, rVaspurakan]),
	iTrueCross				: (iRelic2, [rPalestine, rPalestine, rNobatia, rAksum]),
	iHolyLance				: (iRelic3, [rNorthernSyria, rNorthernSyria, rNorthernSyria, rLebanon, rVaspurakan, rLesserArmenia]),
	iCrownOfThorns			: (iRelic4, [rThrace, rPalestine]),
	iBonesOfTheMagi			: (iRelic5, [rThrace, rAsuristan, rKurdistan, rJibal]),
	iHeadOfJohnTheBaptist	: (iRelic6, [rThrace, rPalestine, rSyria, rLebanon, rNorthernSyria, rJordan, rLowerEgypt, rUpperEgypt, rMakuria, rGreaterArmenia]),
	iCloakOfTheProphet		: (iRelic7, [rGhazni, rGandhar, rKandahar, rBactria, rEasternKhorasan, rWesternKhorasan]),
	iSacredSeal				: (iRelic8, [rHejaz, rHejaz, rHejaz, rSyria, rSyria, rYemen]),
	iHolyBanner				: (iRelic9, [rHejaz, rSyria, rJordan, rUpperEgypt, rLowerEgypt]),
	iBlessedMantle			: (iRelic10, [rUpperEgypt, rLowerEgypt, rHejaz]),
	iBeardOfMuhammad		: (iRelic11, [rHejaz, rYemen, rSyria, rMesopotamia, rJazira, rAsuristan, rOman]),
	iSwordOfAli				: (iRelic12, [rMesopotamia, rMesopotamia, rAsuristan, rAsuristan, rKhuzestan, rJazira, rMazandaran]),
}

# Provinces where lost relics may re-appear
relicRegionsChristian = [rThrace, rPaphlagonia, rCappadocia, rKars, rShirvan, rTrebizond, rPalestine, rSyria, rNorthernSyria, 
rEdessa, rAsuristan, rJibal, rKurdistan, rJordan, rSinai, rLowerEgypt, rUpperEgypt, rNobatia, rMakuria, rAlodia, rAksum, rCyprus,
rGeorgia, rCilicia, rGreaterArmenia, rLesserArmenia, rVaspurakan, rSuqutra, rRhodes, rLebanon]

relicRegionsIslamic = [rShirvan, rAzerbaijan, rSyria, rNorthernSyria, rEdessa, rJazira, rAsuristan, rMesopotamia, rPalestine,
rJordan, rSinai, rLowerEgypt, rUpperEgypt, rHejaz, rYemen, rOman, rMahra, rBahrain, rKhuzestan, rFars, rJibal, rFars, rKerman,
rHormuz, rLuristan, rKurdistan, rYazd, rWesternKhorasan, rEasternKhorasan, rBactria, rSistan, rBalochistan, rSindh, rGhazni,
rGandhar, rKandahar, rMazandaran, rFarghana, rSogd, rLebanon]

# MERCENARIES

# Mercenary name lists
lEastPersianNames = [
	"TXT_KEY_BARB_IRANIAN", 
	"TXT_KEY_BARB_AFGHAN", 
	"TXT_KEY_BARB_BALOCHI", 
	"TXT_KEY_BARB_SISTANI", 
	"TXT_KEY_BARB_TAJIK", 
	"TXT_KEY_BARB_SOGDIAN",
	"TXT_KEY_BARB_KHORASANI",
	"TXT_KEY_BARB_LOHANI",
	"TXT_KEY_BARB_NURISTANI"]
lWestPersianNames = [
	"TXT_KEY_BARB_IRANIAN", 
	"TXT_KEY_BARB_BALOCHI", 
	"TXT_KEY_BARB_KHORASANI",
	"TXT_KEY_BARB_TALYSH",
	"TXT_KEY_BARB_MAZANDARANI",
	"TXT_KEY_BARB_LORI",
	"TXT_KEY_BARB_KERMANI",
	"TXT_KEY_BARB_KURDISH",
	"TXT_KEY_BARB_GILANI"]
lPersianNobleNames = [
	"TXT_KEY_BARB_IRANIAN", 
	"TXT_KEY_BARB_PERSIAN",
	"TXT_KEY_BARB_KHORASANI", 
	"TXT_KEY_BARB_DIHQAN",
	"TXT_KEY_BARB_TURKO_PERSIAN",
	"TXT_KEY_BARB_SOGDIAN"]
lMountaneerNames = [
	"TXT_KEY_BARB_IRANIAN", 
	"TXT_KEY_BARB_ALBANIAN", 
	"TXT_KEY_BARB_AZERI", 
	"TXT_KEY_BARB_KURDISH", 
	"TXT_KEY_BARB_GILANI", 
	"TXT_KEY_BARB_TALYSH", 
	"TXT_KEY_BARB_JABALIYYA"]
lCaucasianNames = [
	"TXT_KEY_BARB_ALAN", 
	"TXT_KEY_BARB_ABKHAZIAN", 
	"TXT_KEY_BARB_SHINAKAN", 
	"TXT_KEY_BARB_ANAZAT", 
	"TXT_KEY_BARB_SHUBOSANI", 
	"TXT_KEY_BARB_ALBANIAN", 
	"TXT_KEY_BARB_KARTLIAN", 
	"TXT_KEY_BARB_KABARDIAN", 
	"TXT_KEY_BARB_SVANIAN", 
	"TXT_KEY_BARB_ADJARIAN", 
	"TXT_KEY_BARB_HEMSHIN", 
	"TXT_KEY_BARB_LAZI", 
	"TXT_KEY_BARB_BAYLAKANI", 
	"TXT_KEY_BARB_KHEVSUR", 
	"TXT_KEY_BARB_PSHAV"]
lCaucasianHorseNames = [
	"TXT_KEY_BARB_ALAN", 
	"TXT_KEY_BARB_AZAT", 
	"TXT_KEY_BARB_AZNAURI", 
	"TXT_KEY_BARB_AZNVAKAN", 
	"TXT_KEY_BARB_KARTLIAN", 
	"TXT_KEY_BARB_DIDEBULI", 
	"TXT_KEY_BARB_KHEVSUR"]
lCaucasianNobleNames = [
	"TXT_KEY_BARB_AZAT", 
	"TXT_KEY_BARB_AZNAURI", 
	"TXT_KEY_BARB_AZNVAKAN", 
	"TXT_KEY_BARB_KARTLIAN", 
	"TXT_KEY_BARB_KHEVSUR", 
	"TXT_KEY_BARB_PSHAV", 
	"TXT_KEY_BARB_SVANIAN"]
lCilicianNames = [
	"TXT_KEY_BARB_CILICIAN", 
	"TXT_KEY_BARB_EDESSAN", 
	"TXT_KEY_BARB_MALATYAN"]
lPaulicianNames = [
	"TXT_KEY_BARB_ARMENIAN", 
	"TXT_KEY_BARB_PAULICIAN"]
lLevantineNames = [
	"TXT_KEY_BARB_SYRIAN", 
	"TXT_KEY_BARB_LEBANESE", 
	"TXT_KEY_BARB_MARONITE", 
	"TXT_KEY_BARB_GREEK"]
lAfghanNames = [
	"TXT_KEY_BARB_ABDALI", 
	"TXT_KEY_BARB_TAREEN", 
	"TXT_KEY_BARB_YUSUFZAI", 
	"TXT_KEY_BARB_MANDANR", 
	"TXT_KEY_BARB_TARKALANI", 
	"TXT_KEY_BARB_MOHMAND", 
	"TXT_KEY_BARB_SHILMANI", 
	"TXT_KEY_BARB_GHILZAI", 
	"TXT_KEY_BARB_NIAZI", 
	"TXT_KEY_BARB_LODHI", 
	"TXT_KEY_BARB_SWATI", 
	"TXT_KEY_BARB_SARWANI", 
	"TXT_KEY_BARB_SURI", 
	"TXT_KEY_BARB_MARWAT", 
	"TXT_KEY_BARB_LOHANI", 
	"TXT_KEY_BARB_DAAVI", 
	"TXT_KEY_BARB_JADOON", 
	"TXT_KEY_BARB_KAKAR", 
	"TXT_KEY_BARB_LUDIN", 
	"TXT_KEY_BARB_NAGHAR", 
	"TXT_KEY_BARB_SAFI", 
	"TXT_KEY_BARB_TARIK", 
	"TXT_KEY_BARB_MAHSUD", 
	"TXT_KEY_BARB_KHATTAK", 
	"TXT_KEY_BARB_AFRIDI"]
lTurkoAfghanNames = [
	"TXT_KEY_BARB_TAREEN", 
	"TXT_KEY_BARB_YUSUFZAI", 
	"TXT_KEY_BARB_MANDANR", 
	"TXT_KEY_BARB_LODHI", 
	"TXT_KEY_BARB_SHERWANI", 
	"TXT_KEY_BARB_SURI", 
	"TXT_KEY_BARB_SINGAM", 
	"TXT_KEY_BARB_KUSELAN", 
	"TXT_KEY_BARB_ILBARI",
	"TXT_KEY_BARB_KHALIL", 
	"TXT_KEY_BARB_KHANZADA", 
	"TXT_KEY_BARB_ROHILLA", 
	"TXT_KEY_BARB_KHALJI"]
lHinduNames = [
	"TXT_KEY_BARB_JAT", 
	"TXT_KEY_BARB_AWAN", 
	"TXT_KEY_BARB_GURJAR", 
	"TXT_KEY_BARB_MARATHA", 
	"TXT_KEY_BARB_BENGALI", 
	"TXT_KEY_BARB_KONKANI"]
lLateHinduNames = [
	"TXT_KEY_BARB_NAWAYATH", 
	"TXT_KEY_BARB_PUNJABI", 
	"TXT_KEY_BARB_JAT", 
	"TXT_KEY_BARB_AWAN", 
	"TXT_KEY_BARB_SAMMAT", 
	"TXT_KEY_BARB_GURJAR", 
	"TXT_KEY_BARB_KHOKHAR", 
	"TXT_KEY_BARB_MARATHA", 
	"TXT_KEY_BARB_BENGALI", 
	"TXT_KEY_BARB_KONKANI", 
	"TXT_KEY_BARB_SIKH", 
	"TXT_KEY_BARB_RATHORE"]
lSindhiNames = [
	"TXT_KEY_BARB_PUNJABI", 
	"TXT_KEY_BARB_GHANDAR", 
	"TXT_KEY_BARB_GAKHAR", 
	"TXT_KEY_BARB_QIQANIYYA", 
	"TXT_KEY_BARB_KHOKHAR", 
	"TXT_KEY_BARB_MUHAJIR"]
lRajputNames = [
	"TXT_KEY_BARB_SOOMRO", 
	"TXT_KEY_BARB_SAMMAT", 
	"TXT_KEY_BARB_SISODIA", 
	"TXT_KEY_BARB_CHATTARI", 
	"TXT_KEY_BARB_BHARI", 
	"TXT_KEY_BARB_TOMARA", 
	"TXT_KEY_BARB_DHANGAR", 
	"TXT_KEY_BARB_JAT", 
	"TXT_KEY_BARB_BHATI", 
	"TXT_KEY_BARB_PANWAR", 
	"TXT_KEY_BARB_MORI", 
	"TXT_KEY_BARB_SODHA", 
	"TXT_KEY_BARB_HARAL", 
	"TXT_KEY_BARB_KHARAL", 
	"TXT_KEY_BARB_LAK", 
	"TXT_KEY_BARB_DADDHA", 
	"TXT_KEY_BARB_PACHAWARA"]
lElephantNames = [
	"TXT_KEY_BARB_PUNJABI", 
	"TXT_KEY_BARB_MARATHA", 
	"TXT_KEY_BARB_BENGALI", 
	"TXT_KEY_BARB_HIMALAYAN", 
	"TXT_KEY_BARB_MALABAR"]
lAfricanNames = [
	"TXT_KEY_BARB_SOMALI", 
	"TXT_KEY_BARB_NUBIAN", 
	"TXT_KEY_BARB_HABASHI", 
	"TXT_KEY_BARB_AMHARA", 
	"TXT_KEY_BARB_SUDANESE", 
	"TXT_KEY_BARB_TIGRAYAN", 
	"TXT_KEY_BARB_ALWA", 
	"TXT_KEY_BARB_BEJA", 
	"TXT_KEY_BARB_ALODIAN", 
	"TXT_KEY_BARB_NOBATIAN", 
	"TXT_KEY_BARB_AFARI", 
	"TXT_KEY_BARB_HAWIYE"]
lLateAfricanNames = [
	"TXT_KEY_BARB_SOMALI", 
	"TXT_KEY_BARB_SUDANESE", 
	"TXT_KEY_BARB_TIGRAYAN", 
	"TXT_KEY_BARB_AFARI", 
	"TXT_KEY_BARB_BEJA", 
	"TXT_KEY_BARB_AMHARA", 
	"TXT_KEY_BARB_OROMO", 
	"TXT_KEY_BARB_HAWIYE"]
lAnatolianNames = [
	"TXT_KEY_BARB_ANATOLIAN", 
	"TXT_KEY_BARB_THRACIAN", 
	"TXT_KEY_BARB_MACEDONIAN", 
	"TXT_KEY_BARB_EPIROTE", 
	"TXT_KEY_BARB_ACHAEAN", 
	"TXT_KEY_BARB_MOESIAN", 
	"TXT_KEY_BARB_CAPPADOCIAN", 
	"TXT_KEY_BARB_GALATIAN", 
	"TXT_KEY_BARB_BITHYNIAN", 
	"TXT_KEY_BARB_CILICIAN"]
lWestBedouinNames = [
	"TXT_KEY_BARB_ZAHRANITE", 
	"TXT_KEY_BARB_ANIZZAH", 
	"TXT_KEY_BARB_BANI_KHALID", 
	"TXT_KEY_BARB_BANI_RASHEED", 
	"TXT_KEY_BARB_BANU_TAMIM", 
	"TXT_KEY_BARB_AL_NUAIM", 
	"TXT_KEY_BARB_MAQIL", 
	"TXT_KEY_BARB_RUWALLAH", 
	"TXT_KEY_BARB_HASHEMITE", 
	"TXT_KEY_BARB_KINANIYYA", 
	"TXT_KEY_BARB_BENI_HASSAN", 
	"TXT_KEY_BARB_BANU_HILAL", 
	"TXT_KEY_BARB_BANU_JAMI", 
	"TXT_KEY_BARB_BANU_SULAYM", 
	"TXT_KEY_BARB_BANU_GHANIYA"]
lEastBedouinNames = [
	"TXT_KEY_BARB_ZAHRANITE", 
	"TXT_KEY_BARB_ANIZZAH", 
	"TXT_KEY_BARB_BANI_KHALID", 
	"TXT_KEY_BARB_BANI_RASHEED", 
	"TXT_KEY_BARB_BANU_TAMIM", 
	"TXT_KEY_BARB_AL_NUAIM", 
	"TXT_KEY_BARB_AZD", 
	"TXT_KEY_BARB_QAHTANITE", 
	"TXT_KEY_BARB_QURAYSH", 
	"TXT_KEY_BARB_SHAMMAR", 
	"TXT_KEY_BARB_GHAMID", 
	"TXT_KEY_BARB_HUWALA", 
	"TXT_KEY_BARB_BANU_LAKHM", 
	"TXT_KEY_BARB_BANU_HANIFA", 
	"TXT_KEY_BARB_BANU_HAMDAN", 
	"TXT_KEY_BARB_BANU_UQAYL", 
	"TXT_KEY_BARB_BANU_AMIR", 
	"TXT_KEY_BARB_BANI_UTBAH", 
	"TXT_KEY_BARB_BANI_NABHAN", 
	"TXT_KEY_BARB_BANI_ASSAD"]
lNorthBedouinNames = [
	"TXT_KEY_BARB_ANIZZAH", 
	"TXT_KEY_BARB_AL_NUAIM", 
	"TXT_KEY_BARB_BANI_KHALID", 
	"TXT_KEY_BARB_BANI_RASHEED", 
	"TXT_KEY_BARB_BENI_HASSAN", 
	"TXT_KEY_BARB_SHAMMAR", 
	"TXT_KEY_BARB_KINANIYYA", 
	"TXT_KEY_BARB_DULAIM", 
	"TXT_KEY_BARB_AL_HADID", 
	"TXT_KEY_BARB_KHAWALID"]
lNorthHorseNames = [
	"TXT_KEY_BARB_PECHENEG", 
	"TXT_KEY_BARB_KIPCHAQ", 
	"TXT_KEY_BARB_CUMAN", 
	"TXT_KEY_BARB_ALAN", 
	"TXT_KEY_BARB_CRIMEAN", 
	"TXT_KEY_BARB_CIRCASSIAN", 
	"TXT_KEY_BARB_UZ", 
	"TXT_KEY_BARB_KARACHAY"]
lTurcopoleNames = [
	"TXT_KEY_BARB_TURCOPOLE", 
	"TXT_KEY_BARB_ARMENIAN", 
	"TXT_KEY_BARB_CILICIAN", 
	"TXT_KEY_BARB_CIRCASSIAN"]
lTurkoPersianNames = [
	"TXT_KEY_BARB_TURKISH", 
	"TXT_KEY_BARB_TURKO_PERSIAN", 
	"TXT_KEY_BARB_IRANIAN", 
	"TXT_KEY_BARB_AZERI", 
	"TXT_KEY_BARB_KHALAJ", 
	"TXT_KEY_BARB_QASHQAI"]
lEastTurkicNames = [
	"TXT_KEY_BARB_TURKISH", 
	"TXT_KEY_BARB_TURKOMAN", 
	"TXT_KEY_BARB_TURKO_PERSIAN", 
	"TXT_KEY_BARB_OGHUZ", 
	"TXT_KEY_BARB_QANQLI", 
	"TXT_KEY_BARB_IRANIAN", 
	"TXT_KEY_BARB_KHALAJ", 
	"TXT_KEY_BARB_QASHQAI", 
	"TXT_KEY_BARB_KARAKALPAK", 
	"TXT_KEY_BARB_KARA_KHANID"]
lWestTurkicNames = [
	"TXT_KEY_BARB_TURKISH", 
	"TXT_KEY_BARB_TURKOMAN", 
	"TXT_KEY_BARB_TURKO_PERSIAN", 
	"TXT_KEY_BARB_OGHUZ", 
	"TXT_KEY_BARB_AFSHARI", 
	"TXT_KEY_BARB_QAJAR"]
lEarlyTurkicNames = [
	"TXT_KEY_BARB_TURKISH", 
	"TXT_KEY_BARB_SIMJURID", 
	"TXT_KEY_BARB_QARLUQ", 
	"TXT_KEY_BARB_KARA_KHANID", 
	"TXT_KEY_BARB_SOGDIAN"]
lLateTurkicNames = [
	"TXT_KEY_BARB_TURKISH", 
	"TXT_KEY_BARB_TURKOMAN", 
	"TXT_KEY_BARB_TURKO_PERSIAN", 
	"TXT_KEY_BARB_OGHUZ", 
	"TXT_KEY_BARB_IRANIAN", 
	"TXT_KEY_BARB_KHALAJ", 
	"TXT_KEY_BARB_QASHQAI", 
	"TXT_KEY_BARB_QAJAR", 
	"TXT_KEY_BARB_KARAKALPAK", 
	"TXT_KEY_BARB_TURKO_MONGOL", 
	"TXT_KEY_BARB_AZERI", 
	"TXT_KEY_BARB_UZBEK", 
	"TXT_KEY_BARB_HAZARA", 
	"TXT_KEY_BARB_KARA_KOYUNLU"]
lKurdishNames = [
	"TXT_KEY_BARB_SYRIAN", 
	"TXT_KEY_BARB_KURDISH", 
	"TXT_KEY_BARB_PESHMERGA", 
	"TXT_KEY_BARB_KHASSEKI", 
	"TXT_KEY_BARB_MUHAJIR"]
lSyrianNames = [
	"TXT_KEY_BARB_HARAFISHA", 
	"TXT_KEY_BARB_MUTATAWWIA", 
	"TXT_KEY_BARB_SYRIAN", 
	"TXT_KEY_BARB_KURDISH", 
	"TXT_KEY_BARB_PALESTINIAN", 
	"TXT_KEY_BARB_AHDATH", 
	"TXT_KEY_BARB_DRUZE"]
lSyrianArcherNames = [
	"TXT_KEY_BARB_SYRIAN", 
	"TXT_KEY_BARB_KURDISH", 
	"TXT_KEY_BARB_PALESTINIAN", 
	"TXT_KEY_BARB_LEBANESE", 
	"TXT_KEY_BARB_AL_ASHAIR", 
	"TXT_KEY_BARB_DRUZE"]
lIraqiNames = [
	"TXT_KEY_BARB_HARAFISHA", 
	"TXT_KEY_BARB_IRAQI", 
	"TXT_KEY_BARB_KURDISH", 
	"TXT_KEY_BARB_AYYARUN", 
	"TXT_KEY_BARB_FITYAN", 
	"TXT_KEY_BARB_SHUTTAR", 
	"TXT_KEY_BARB_MUHAJIR"]
lArabNames = [
	"TXT_KEY_BARB_ARAB", 
	"TXT_KEY_BARB_SYRIAN", 
	"TXT_KEY_BARB_KURDISH", 
	"TXT_KEY_BARB_DRUZE"]
lArabNobleNames = [
	"TXT_KEY_BARB_ARAB", 
	"TXT_KEY_BARB_SYRIAN", 
	"TXT_KEY_BARB_KURDISH", 
	"TXT_KEY_BARB_MUHAJIR"]
lKnightNames = [
	"TXT_KEY_BARB_FRANKISH", 
	"TXT_KEY_BARB_GERMAN", 
	"TXT_KEY_BARB_NORMAN", 
	"TXT_KEY_BARB_SICILIAN", 
	"TXT_KEY_BARB_FRISIAN", 
	"TXT_KEY_BARB_PROVENCAL"]
lFrenchNames = [
	"TXT_KEY_BARB_FRANKISH", 
	"TXT_KEY_BARB_NORMAN", 
	"TXT_KEY_BARB_SICILIAN", 
	"TXT_KEY_BARB_AMALFIAN", 
	"TXT_KEY_BARB_PROVENCAL", 
	"TXT_KEY_BARB_TOULOUSAN", 
	"TXT_KEY_BARB_AQUITANIAN"]
lSailorNames = [
	"TXT_KEY_BARB_GENOAN", 
	"TXT_KEY_BARB_LIGURIAN", 
	"TXT_KEY_BARB_VENETIAN", 
	"TXT_KEY_BARB_PISAN", 
	"TXT_KEY_BARB_SIENESE", 
	"TXT_KEY_BARB_SICILIAN"]
lVenetianNames = [
	"TXT_KEY_BARB_VENETIAN"]
lNaffatunNames = [
	"TXT_KEY_BARB_IRAQI", 
	"TXT_KEY_BARB_AHVAZIAN", 
	"TXT_KEY_BARB_SYRIAN", 
	"TXT_KEY_BARB_KURDISH", 
	"TXT_KEY_BARB_JAZIRAN", 
	"TXT_KEY_BARB_ARABIAN"]
lMaghrebNames = [
	"TXT_KEY_BARB_MAGHREBI", 
	"TXT_KEY_BARB_BERBER", 
	"TXT_KEY_BARB_MOORISH", 
	"TXT_KEY_BARB_ANDALUSIAN", 
	"TXT_KEY_BARB_TRIPOLITANIAN", 
	"TXT_KEY_BARB_SOUSSAN", 
	"TXT_KEY_BARB_TUNISIAN", 
	"TXT_KEY_BARB_MAHDIAN", 
	"TXT_KEY_BARB_IFRIQIYAN", 
	"TXT_KEY_BARB_ZIRID"]
lAssassinNames = [
	"TXT_KEY_BARB_SYRIAN", 
	"TXT_KEY_BARB_DAYLAMI", 
	"TXT_KEY_BARB_AINSARII", 
	"TXT_KEY_BARB_SHAHDIZ", 
	"TXT_KEY_BARB_LAMASSAR"]
lDaylamiNames = [
	"TXT_KEY_BARB_RASHT", 
	"TXT_KEY_BARB_ASTARA", 
	"TXT_KEY_BARB_LAHIJAN", 
	"TXT_KEY_BARB_TALYSH", 
	"TXT_KEY_BARB_MASALAR", 
	"TXT_KEY_BARB_MANJIL", 
	"TXT_KEY_BARB_LANGARUD"]
lMamlukNames = [
	"TXT_KEY_BARB_QARA_GHULAM", 
	"TXT_KEY_BARB_CIRCASSIAN", 
	"TXT_KEY_BARB_KIPCHAQ", 
	"TXT_KEY_BARB_KURDISH", 
	"TXT_KEY_BARB_SYRIAN", 
	"TXT_KEY_BARB_TOASSIN", 
	"TXT_KEY_BARB_AL_HALQA"]
lKipchakNames = [
	"TXT_KEY_BARB_KIPCHAQ",	
	"TXT_KEY_BARB_CUMAN", 
	"TXT_KEY_BARB_KARAKALPAK"]
lVarangianNames = [
	"TXT_KEY_BARB_SCANDINAVIAN", 
	"TXT_KEY_BARB_DANISH", 
	"TXT_KEY_BARB_SWEDISH", 
	"TXT_KEY_BARB_NORWEGIAN", 
	"TXT_KEY_BARB_ANGLO_SAXON", 
	"TXT_KEY_BARB_RUS"]
lBulgarianNames = [
	"TXT_KEY_BARB_THRACIAN", 
	"TXT_KEY_BARB_MOESIAN", 
	"TXT_KEY_BARB_DOBRUJAN", 
	"TXT_KEY_BARB_STRANJAN"]
lEasternCamelNames = [
	"TXT_KEY_BARB_PUNJABI", 
	"TXT_KEY_BARB_KHORASANI", 
	"TXT_KEY_BARB_BALOCHI", 
	"TXT_KEY_BARB_SISTANI"]
lMarathaNames = [
	"TXT_KEY_BARB_ADKARE", 
	"TXT_KEY_BARB_AGLAVE", 
	"TXT_KEY_BARB_AHER", 
	"TXT_KEY_BARB_ANVALE", 
	"TXT_KEY_BARB_ASVE", 
	"TXT_KEY_BARB_AKOLKAR", 
	"TXT_KEY_BARB_AVTADE", 
	"TXT_KEY_BARB_BADAD", 
	"TXT_KEY_BARB_BADAL", 
	"TXT_KEY_BARB_BAGAL", 
	"TXT_KEY_BARB_BAKAR", 
	"TXT_KEY_BARB_BAVCHIKAR", 
	"TXT_KEY_BARB_BAVDHANKAR", 
	"TXT_KEY_BARB_BHADIRGE", 
	"TXT_KEY_BARB_BHAGAT", 
	"TXT_KEY_BARB_BHAKAD", 
	"TXT_KEY_BARB_BHATMARE", 
	"TXT_KEY_BARB_BHINGARI", 
	"TXT_KEY_BARB_BHUJVAR", 
	"TXT_KEY_BARB_CHALKHE", 
	"TXT_KEY_BARB_CHAUDHARE", 
	"TXT_KEY_BARB_CHAVAT", 
	"TXT_KEY_BARB_DALVI", 
	"TXT_KEY_BARB_DEVKAR", 
	"TXT_KEY_BARB_DHANAVDE", 
	"TXT_KEY_BARB_DHUMAL", 
	"TXT_KEY_BARB_DIVTHANKAR", 
	"TXT_KEY_BARB_GAVSEKAR", 
	"TXT_KEY_BARB_GHADSHI", 
	"TXT_KEY_BARB_GHANWAT", 
	"TXT_KEY_BARB_GHURE", 
	"TXT_KEY_BARB_INDULKAR", 
	"TXT_KEY_BARB_JADHAV", 
	"TXT_KEY_BARB_JUVEKAR", 
	"TXT_KEY_BARB_KABADE", 
	"TXT_KEY_BARB_KAMEKAR", 
	"TXT_KEY_BARB_KANDAR", 
	"TXT_KEY_BARB_KANDVI", 
	"TXT_KEY_BARB_KARVALKAR", 
	"TXT_KEY_BARB_KATHVATE", 
	"TXT_KEY_BARB_KHANDEKAR", 
	"TXT_KEY_BARB_KHARDEKAR", 
	"TXT_KEY_BARB_KIRDATTA", 
	"TXT_KEY_BARB_LABHADE", 
	"TXT_KEY_BARB_LAGHATE", 
	"TXT_KEY_BARB_LAGVANKAR", 
	"TXT_KEY_BARB_MANDAVKAR", 
	"TXT_KEY_BARB_MANVE", 
	"TXT_KEY_BARB_MAREKARI", 
	"TXT_KEY_BARB_MUKHEKAR", 
	"TXT_KEY_BARB_MUNDEKAR", 
	"TXT_KEY_BARB_NALAWADE", 
	"TXT_KEY_BARB_NIMBALKAR", 
	"TXT_KEY_BARB_PACHUNDKAR", 
	"TXT_KEY_BARB_PADALKAR", 
	"TXT_KEY_BARB_PADIYAR", 
	"TXT_KEY_BARB_PAGHAM", 
	"TXT_KEY_BARB_PALAV", 
	"TXT_KEY_BARB_PANDHRE", 
	"TXT_KEY_BARB_PANDIT", 
	"TXT_KEY_BARB_PARAB", 
	"TXT_KEY_BARB_PATADE", 
	"TXT_KEY_BARB_PATANKAR", 
	"TXT_KEY_BARB_PAVAR", 
	"TXT_KEY_BARB_RAJGIRE", 
	"TXT_KEY_BARB_RASAL", 
	"TXT_KEY_BARB_SALGAR", 
	"TXT_KEY_BARB_SALIM", 
	"TXT_KEY_BARB_SALVI", 
	"TXT_KEY_BARB_SANMUKH", 
	"TXT_KEY_BARB_SARANG", 
	"TXT_KEY_BARB_SATAL", 
	"TXT_KEY_BARB_SAVASHE", 
	"TXT_KEY_BARB_SHANKAR", 
	"TXT_KEY_BARB_SHIPALKAR", 
	"TXT_KEY_BARB_SHIRASVADE", 
	"TXT_KEY_BARB_SURVASI", 
	"TXT_KEY_BARB_TAKVADEKAR", 
	"TXT_KEY_BARB_TANPURE", 
	"TXT_KEY_BARB_TELVEKAR", 
	"TXT_KEY_BARB_UPALKAR", 
	"TXT_KEY_BARB_VADKAR", 
	"TXT_KEY_BARB_VAGHMARE", 
	"TXT_KEY_BARB_YADAV", 
	"TXT_KEY_BARB_WADJE"]
lGalleyNames = [
	"TXT_KEY_BARB_VENETIAN", 
	"TXT_KEY_BARB_GENOAN", 
	"TXT_KEY_BARB_SICILIAN", 
	"TXT_KEY_BARB_LIGURIAN", 
	"TXT_KEY_BARB_PISAN", 
	"TXT_KEY_BARB_AMALFIAN", 
	"TXT_KEY_BARB_NEAPOLITAN", 
	"TXT_KEY_BARB_RAGUSAN", 
	"TXT_KEY_BARB_SIENESE", 
	"TXT_KEY_BARB_ANCONIAN"]
lMaghrebGalleyNames = [
	"TXT_KEY_BARB_MAGHREBI", 
	"TXT_KEY_BARB_TRIPOLITANIAN", 
	"TXT_KEY_BARB_SOUSSAN", 
	"TXT_KEY_BARB_TUNISIAN", 
	"TXT_KEY_BARB_MAHDIAN"]
lDhowNames = [
	"TXT_KEY_BARB_SINDHI", 
	"TXT_KEY_BARB_MALACCAN", 
	"TXT_KEY_BARB_YEMENI", 
	"TXT_KEY_BARB_SOMALI", 
	"TXT_KEY_BARB_ACEH"]

# Mercenary unit list ( UnitType, NameList, PrereqReligions/Year, set(PrereqProvinces), [ Corporations ]  )
tMercenaries = ( 
(iJavelinman,				lAnatolianNames,	[iOrthodoxy],				set([rThrace, Thessaly, rCentralGreece, rMorea, rEpirus, rCrete, rAsia, rBithynia, rLycia, rPontus, rGalatia, rPaphlagonia, rCilicia, rCappadocia, rLesserArmenia, rRhodes, rCyprus])),
(iJavelinman_Caucasian,		lMountaneerNames,	[],							set([rAsuristan, rAzerbaijan, rShirvan, rMazandaran, rJibal, rKurdistan, rJazira])),
(iJavelinman_Turkish,		lEastPersianNames,	[iSunni, iShia],			set([rWesternKhorasan, rEasternKhorasan, rSogd, rKhwarezm, rFarghana, rBactria, rHindukush])),
(iJavelinman_African,       lAfricanNames,		[],							set([rAlodia, rMakuria, rNobatia, rUpperEgypt, rLowerEgypt, rAksum, rMerebMellash, rYemen, rLibya])),
(iJavelinman_Indian,        lHinduNames,		[],							set([rUttarBharat, rGujarat, rGird, rRajputana, rMalwa, rMaharashtra])),
(iArcher_Caucasian,			lCaucasianNames,	[iOrthodoxy, iCatholicism],	set([rGeorgia, rGreaterArmenia, rKars, rShirvan, rAzerbaijan, rVaspurakan, rLesserArmenia, rTrebizond, rCappadocia, rDagestan])),
(iArcher_Caucasian,			lCilicianNames,		[iOrthodoxy, iCatholicism],	set([rCilicia, rEdessa, rNorthernSyria])),
(iArcher_Arab,				lSyrianArcherNames,	[iSunni, iShia],			set([rLowerEgypt, rPalestine, rLebanon, rSyria, rNorthernSyria, rJordan, rJazira])),
(iArcher_Arab,				lIraqiNames,		[iSunni, iShia],			set([rAsuristan, rMesopotamia, rKhuzestan])),
(iArcher_Bedouin,			lWestBedouinNames,	[iSunni, iShia],			set([rJordan, rHejaz, rSyria, rJazira, rMesopotamia, rUpperEgypt, rNobatia, rMakuria, rAlodia])),
(iArcher_Bedouin,			lEastBedouinNames,	[iSunni, iShia],			set([rHejaz, rYemen, rHadhramaut, rMahra, rOman, rBahrain, rMesopotamia])),
(iArcher_African,			lAfricanNames,		[],							set([rAlodia, rMakuria, rNobatia, rUpperEgypt, rLowerEgypt, rAksum, rMerebMellash, rYemen, rLibya])),
(iArcher_Indian,			lHinduNames,		[],							set([rUttarBharat, rGujarat, rGird, rRajputana, rMalwa, rMaharashtra])),
(iArcher_Indian,			lSindhiNames,		[],							set([rSindh, rPunjab, rDuggar])),
(iArcher_Persian,			lWestPersianNames,	[],							set([rKhuzestan, rJibal, rLuristan, rKurdistan, rKerman, rFars, rYazd, rMazandaran, rWesternKhorasan, rAzerbaijan])),
(iArcher_Turkish,			lEarlyTurkicNames,	[],							set([rEasternKhorasan, rSistan, rBalochistan, rSogd, rBactria, rMakran])),
(iArcher_Syrian,			lLevantineNames,	[iOrthodoxy, iCatholicism],	set([rLebanon])),
(iMarksman_Arab, 			lArabNames,			[],							set([rLowerEgypt, rPalestine, rSyria, rNorthernSyria, rJordan, rJazira, rLibya])),
(iMarksman_Turkish, 		lTurkoPersianNames,	[iSunni, iShia],			set([rCappadocia, rLesserArmenia, rJazira, rAsuristan, rJibal, rAzerbaijan, rKurdistan, rLuristan, rKerman, rFars, rMazandaran])),
(iMarksman_Turkish, 		lLateTurkicNames,	[iSunni, iShia],			set([rWesternKhorasan, rEasternKhorasan, rSistan, rBalochistan, rSogd, rKhwarezm, rBactria])),
(iMarksman_Indian, 			lHinduNames,		[],							set([rUttarBharat, rGujarat, rGird, rRajputana, rMalwa, rMaharashtra, rPunjab])),
(iMarksman_Bedouin,			lWestBedouinNames,	[iSunni, iShia],			set([rJordan, rHejaz, rSyria, rJazira, rMesopotamia, rUpperEgypt, rNobatia, rMakuria, rAlodia])),
(iMarksman_Caucasian,		lCilicianNames,		[iOrthodoxy, iCatholicism],	set([rCilicia, rEdessa, rNorthernSyria])),
(iSpearman_Harafisha,		lArabNames,			[],							set([rLowerEgypt, rPalestine, rSyria, rNorthernSyria, rJordan, rJazira, rLibya])),
(iSpearman_Harafisha,		lIraqiNames,		[iSunni, iShia],			set([rAsuristan, rMesopotamia, rKhuzestan])),
(iSpearman_Bedouin,			lNorthBedouinNames,	[iSunni, iShia],			set([rPalestine, rSyria, rJazira, rMesopotamia])),
(iSpearman_Caucasian,		lCaucasianNames,	[iOrthodoxy, iCatholicism],	set([rGeorgia, rGreaterArmenia, rKars, rShirvan, rAzerbaijan, rVaspurakan, rLesserArmenia, rTrebizond, rCappadocia, rDagestan])),
(iSpearman_Caucasian,		lCilicianNames,		[iOrthodoxy, iCatholicism],	set([rCilicia, rEdessa, rNorthernSyria])),
(iSpearman_Indian,			lHinduNames,		[],							set([rUttarBharat, rGird, rRajputana, rMalwa, rMaharashtra, rGujarat])),
(iSpearman_Indian,			lSindhiNames,		[],							set([rSindh, rPunjab, rDuggar])),
(iSpearman_African,			lAfricanNames,		[],							set([rAlodia, rMakuria, rNobatia, rUpperEgypt, rLowerEgypt, rAksum, rMerebMellash, rYemen, rLibya])),
(iSpearman_Turkish,			lWestPersianNames,	[],							set([rKhuzestan, rJibal, rLuristan, rKurdistan, rKerman, rFars, rYazd, rMazandaran, rWesternKhorasan, rAzerbaijan])),
(iSpearman_Turkish,			lEastPersianNames,	[],							set([rEasternKhorasan, rSistan, rBalochistan, rSogd, rBactria, rMakran])),
(iHeavySpearman_Arab,		lArabNobleNames,	[],							set([rPalestine, rSyria, rNorthernSyria, rJazira])),
(iHeavySpearman_Indian,		lHinduNames,		[],							set([rUttarBharat, rGujarat, rGird, rRajputana, rMalwa, rMaharashtra])),
(iHeavySpearman_Indian,		lSindhiNames,		[],							set([rSindh, rPunjab, rDuggar])),
(iHeavySpearman_Kipchak,	lNorthHorseNames,	[],							set([rGeorgia, rKars, rShirvan, rAzerbaijan, rGreaterArmenia, rTrebizond, rThrace, rBulgaria, Thessaly, rSerbia, rDagestan])),
(iAxeman_Paulician,			lPaulicianNames,	[iCatholicism,iSunni,iShia],set([rNorthernSyria, rLesserArmenia, rLowerEgypt])),
(iAxeman_Kurdish,			lKurdishNames,		[],							set([rSyria, rNorthernSyria, rJazira, rAsuristan, rKurdistan])),
(iAxeman_Caucasian,			lCilicianNames,		[iOrthodoxy, iCatholicism],	set([rEdessa, rCilicia, rNorthernSyria])),
(iAxeman_Caucasian,			lCaucasianNames,	[iOrthodoxy, iCatholicism],	set([rGeorgia, rGreaterArmenia, rKars, rShirvan, rAzerbaijan, rVaspurakan, rLesserArmenia, rTrebizond, rCappadocia, rDagestan])),
(iAxeman_Persian,			lWestPersianNames,	[iSunni, iShia],			set([rKhuzestan, rJibal, rLuristan, rKurdistan, rKerman, rFars, rYazd, rMazandaran, rWesternKhorasan, rAzerbaijan])),
(iAxeman_Persian,			lEastPersianNames,	[iSunni, iShia],			set([rEasternKhorasan, rSistan, rBalochistan, rSogd, rBactria, rMakran])),
(iMaceman_Harafisha,		lSyrianNames,		[iSunni, iShia],			set([rLowerEgypt, rPalestine, rSyria, rNorthernSyria, rJordan, rJazira])),
(iMaceman_Turkish,			lTurkoPersianNames,	[iSunni, iShia],			set([rCappadocia, rLesserArmenia, rJazira, rAsuristan, rJibal, rAzerbaijan])),
(iSwordsman_Arab,			lArabNames,			[iSunni, iShia],			set([rLowerEgypt, rPalestine, rLebanon, rSyria, rNorthernSyria, rJazira])),
(iSwordsman_Indian,			lRajputNames,		[],							set([rUttarBharat, rGujarat, rGird, rRajputana, rMalwa, rMaharashtra])),
(iSwordsman_Indian,			lRajputNames,		[],							set([rSindh, rPunjab, rDuggar])),
(iSwordsman_Kipchak,		lNorthHorseNames,	[],							set([rGeorgia, rKars, rShirvan, rAzerbaijan, rGreaterArmenia, rThrace, rBulgaria, Thessaly, rSerbia, rDagestan])),
(iSwordsman_Caucasian,		lCaucasianNobleNames,[],						set([rGeorgia, rKars, rShirvan, rGreaterArmenia, rTrebizond, rDagestan])),
(iSwordsman_Persian,		lWestPersianNames,	[iSunni, iShia],			set([rKhuzestan, rJibal, rLuristan, rKurdistan, rKerman, rFars, rYazd, rMazandaran, rWesternKhorasan, rAzerbaijan])),
(iSwordsman_Persian,		lEastPersianNames,	[iSunni, iShia],			set([rEasternKhorasan, rSistan, rBalochistan, rSogd, rBactria, rMakran])),
(iHeavySwordsman_Generic,	lWestPersianNames,	[iSunni, iShia],			set([rKhuzestan, rJibal, rLuristan, rKurdistan, rKerman, rFars, rYazd, rMazandaran, rWesternKhorasan, rAzerbaijan])),
(iHeavySwordsman_Generic,	lEastPersianNames,	[iSunni, iShia],			set([rEasternKhorasan, rSistan, rBalochistan, rSogd, rBactria, rMakran])),
(iHeavySwordsman_Afghan,	lTurkoAfghanNames,	[],							set([rPunjab, rGandhar, rDuggar, rUttarBharat, rHindukush, rKandahar, rGhazni])),
(iHeavySwordsman_Rajput,	lRajputNames,		[],							set([rUttarBharat, rGird, rRajputana, rMalwa, rGujarat])),
(iHorseArcher_Kipchak,		lNorthHorseNames,	[],							set([rGeorgia, rGreaterArmenia, rKars, rShirvan, rAzerbaijan, rVaspurakan, rLesserArmenia, rTrebizond, rCappadocia, rDagestan])),
(iHorseArcher_Christian,	lTurcopoleNames,	[iOrthodoxy, iCatholicism],	set([rSyria, rNorthernSyria, rPalestine, rEdessa, rLesserArmenia, rCappadocia, rGalatia, rCilicia, rVaspurakan, rGreaterArmenia, rKars, rBulgaria, Thessaly])),
(iHorseArcher_Turkish,		lWestTurkicNames,	[iSunni, iShia],			set([rCappadocia, rGalatia, rBithynia, rLesserArmenia, rSyria, rNorthernSyria, rJazira, rAsuristan, rMesopotamia, rKhuzestan, rBulgaria, Thessaly])),
(iHorseArcher_Turkish,		lEastTurkicNames,	[iSunni, iShia],			set([rEasternKhorasan, rSistan, rBalochistan, rGhazni, rSogd, rKhwarezm, rFarghana, rBactria, rMakran])),
(iHorseArcher_Turkish,		lEastTurkicNames,	[iSunni, iShia],			set([rJibal, rLuristan, rKurdistan, rKerman, rFars, rYazd, rMazandaran, rWesternKhorasan, rAzerbaijan])),
(iHeavyHorseArcher_Turkish,	lWestTurkicNames,	[iSunni, iShia],			set([rCappadocia, rGalatia, rBithynia, rLesserArmenia, rSyria, rNorthernSyria, rJazira, rAsuristan, rMesopotamia, rKhuzestan, rBulgaria, Thessaly])),
(iHeavyHorseArcher_Turkish,	lLateTurkicNames,	[iSunni, iShia],			set([rJibal, rLuristan, rKurdistan, rKerman, rFars, rYazd, rMazandaran, rWesternKhorasan, rEasternKhorasan, rSistan, rBalochistan, rGhazni, rSogd, rKhwarezm, rFarghana, rBactria, rMakran, rAzerbaijan])),
(iSkirmisher_Arab,			lArabNobleNames,	[iSunni, iShia],			set([rLowerEgypt, rPalestine, rSyria, rNorthernSyria, rJordan, rJazira, rLibya])),
(iHorseman_Bedouin,			lWestBedouinNames,	[iSunni, iShia],			set([rJordan, rHejaz, rSyria, rJazira, rMesopotamia, rUpperEgypt, rNobatia, rMakuria, rAlodia, rLibya])),
(iHorseman_Bedouin,			lEastBedouinNames,	[iSunni, iShia],			set([rHejaz, rYemen, rHadhramaut, rMahra, rOman, rBahrain])),
(iHorseman_Indian,			lRajputNames,		[],							set([rUttarBharat, rGujarat, rGird, rRajputana, rMalwa, rMaharashtra])),
(iHorseman_Indian,			lRajputNames,		[],							set([rSindh, rPunjab, rDuggar])),
(iHorseman_Persian,			lPersianNobleNames,	[iSunni, iShia],			set([rKhuzestan, rJibal, rLuristan, rKurdistan, rKerman, rFars, rYazd, rMazandaran, rWesternKhorasan, rEasternKhorasan, rBactria, rAzerbaijan])),
(iMountedInfantry_Persian,	lPersianNobleNames,	[iSunni, iShia],			set([rKhuzestan, rJibal, rLuristan, rKurdistan, rKerman, rFars, rYazd, rMazandaran, rWesternKhorasan, rEasternKhorasan, rBactria, rAzerbaijan])),
(iLancer_Turkish,			lEastTurkicNames,	[iSunni, iShia],			set([rCappadocia, rGalatia, rBithynia, rLesserArmenia, rSyria, rNorthernSyria, rJazira, rAsuristan, rMesopotamia, rKhuzestan, rBulgaria, Thessaly])),
(iLancer_Turkish,			lEastTurkicNames,	[iSunni, iShia],			set([rJibal, rLuristan, rKurdistan, rKerman, rFars, rYazd, rMazandaran, rWesternKhorasan, rEasternKhorasan, rSistan, rBalochistan, rGhazni, rSogd, rKhwarezm, rFarghana, rBactria, rMakran])),
(iLancer_Kipchak,			lKipchakNames,		[],							set([rGeorgia, rShirvan, rKhwarezm, rDagestan])),
(iLancer_Syrian,			lArabNobleNames,	[iSunni, iShia],			set([rLowerEgypt, rPalestine, rSyria, rLebanon, rNorthernSyria, rJordan, rJazira])),
(iLancer_Frankish,			lKnightNames,		[iOrthodoxy],				set([rThrace, rAsia, rLycia, rCilicia, rCyprus, rNorthernSyria, Thessaly, rCentralGreece, rMorea, rSerbia, rEpirus, rCrete, rCephalonia])),
(iHeavyLancer_Mamluk,		lMamlukNames,		[iSunni, iShia],			set([rLowerEgypt, rPalestine, rSyria, rMesopotamia])),
(iHeavyLancer_Frankish,		lKnightNames,		[iOrthodoxy],				set([rThrace, rAsia, rLycia, rCilicia, rCyprus, rNorthernSyria, Thessaly, rCentralGreece, rMorea, rSerbia, rEpirus, rCrete, rCephalonia])),
(iHeavyLancer_Indian,		lRajputNames,		[],							set([rUttarBharat, rGird, rRajputana, rMalwa, rGujarat])),
(iCamelArcher,				lEastBedouinNames,	[iSunni, iShia],			set([rHejaz, rYemen, rHadhramaut, rMahra, rOman, rBahrain, rMesopotamia])),
(iCamelArcher,				lWestBedouinNames,	[iSunni, iShia],			set([rUpperEgypt, rNobatia, rMakuria, rAlodia, rMerebMellash])),
(iCamelRider,				lEastBedouinNames,	[iSunni, iShia],			set([rHejaz, rYemen, rHadhramaut, rMahra, rOman, rBahrain])),
(iCamelGunner,				lEastBedouinNames,	[iSunni, iShia],			set([rHejaz, rYemen, rHadhramaut, rMahra, rOman, rBahrain])),
(iCamelGunner_Indian,		lLateHinduNames,	[],							set([rWesternKhorasan, rEasternKhorasan, rBalochistan, rSistan, rPunjab, rSindh, rKandahar, rGhazni])),
(iLightCavalry_Bedouin,		lEastBedouinNames,	[iSunni, iShia],			set([rYemen, rHejaz, rHadhramaut, rMahra, rOman, rBahrain, rJordan, rSyria, rJazira, rMesopotamia])),
(iArquebusier_African, 		lLateAfricanNames,	[],							set([rAlodia, rMakuria, rNobatia, rUpperEgypt, rAksum, rMerebMellash, rLibya])),
(iArquebusier_Indian, 		lLateHinduNames,	[],							set([rUttarBharat, rDuggar, rPunjab, rSindh, rGujarat, rGird, rRajputana, rMalwa, rMaharashtra, rKarnataka, rGoa])),
(iArquebusier_Bedouin, 		lNorthBedouinNames,	[iSunni, iShia],			set([rPalestine, rSyria, rJazira, rMesopotamia])),
(iMusketman_Indian, 		lLateHinduNames,	[],							set([rUttarBharat, rDuggar, rPunjab, rSindh, rGujarat, rGird, rRajputana, rMalwa, rMaharashtra, rKarnataka, rGoa])),
(iMusketman_Bedouin, 		lNorthBedouinNames,	[iSunni, iShia],			set([rPalestine, rSyria, rJazira, rMesopotamia])),
(iWarElephant,				lElephantNames,		[],							set([rUttarBharat, rDuggar, rPunjab, rSindh, rGujarat, rGird, rRajputana, rMalwa, rMaharashtra, rKarnataka, rGoa, rGandhar, rGhazni, rBalochistan])),
(iHeavyWarElephant,			lElephantNames,		[],							set([rUttarBharat, rDuggar, rPunjab, rSindh, rGujarat, rGird, rRajputana, rMalwa, rMaharashtra, rKarnataka, rGoa, rGandhar, rGhazni, rBalochistan])),
(iDaylamiTribesman,			lDaylamiNames,		[iSunni, iShia],			set([rMazandaran, rJibal, rWesternKhorasan, rEasternKhorasan])),
(iDaylamiInfantry,			lDaylamiNames,		[iSunni, iShia],			set([rMazandaran, rJibal, rWesternKhorasan, rEasternKhorasan])),
(iVarangianGuard,			lVarangianNames,	[iOrthodoxy],				set([rConstantinople])),
(iZanjiSwordsman,			lAfricanNames,		[],							set([rAlodia, rMakuria, rNobatia, rUpperEgypt, rLowerEgypt, rAksum, rMerebMellash, rLibya])),
(iZanjiSpearman,			lAfricanNames,		[],							set([rAlodia, rMakuria, rNobatia, rUpperEgypt, rLowerEgypt, rAksum, rMerebMellash, rLibya])),
(iPashtunWarrior,			lAfghanNames,		[],							set([rHindukush, rGandhar, rGhazni, rKandahar, rBalochistan, rSistan, rPunjab])),
(iPashtunCavalry,			lAfghanNames,		[],							set([rHindukush, rGandhar, rGhazni, rKandahar, rBalochistan, rSistan, rPunjab])),
(iAfghanInfantry,			lAfghanNames,		[],							set([rGandhar, rGhazni, rKandahar, rDuggar, rPunjab, rUttarBharat])),
(iAfghanPikeman,			lAfghanNames,		[],							set([rGandhar, rGhazni, rKandahar, rDuggar, rPunjab, rUttarBharat])),
(iMarathaWarrior,			lMarathaNames,		[],							set([rMaharashtra, rMalwa, rGujarat, rKarnataka, rGoa])),
(iMarathaCavalry,			lMarathaNames,		[],							set([rMaharashtra, rMalwa, rGujarat, rKarnataka, rGoa])),
(iBulgarianRaider,			lBulgarianNames,	[iOrthodoxy],				set([rThrace, rSerbia, rBulgaria, Thessaly])),
(iNaffatun,					lNaffatunNames,		[iSunni, iShia],			set([rMesopotamia, rJazira, rSyria])),
(iMarine,					lMaghrebNames,		[iSunni, iShia],			set([rLowerEgypt, rCyprus, rPalestine, rLebanon, rRhodes, rCrete])),
(iManAtArms,				lFrenchNames,		[iOrthodoxy, iCatholicism],	set([rPalestine, rNorthernSyria, rLebanon, rCilicia, rCyprus, rCrete, rEpirus])),
(iItalianCrossbowman,		lSailorNames,		[iOrthodoxy, iCatholicism],	set(lCompanyRegions[iGenoans]), [iVenetians, iGenoans]),
(iItalianMaceman,			lSailorNames,		[iCatholicism],				set(lCompanyRegions[iVenetians]), [iVenetians, iGenoans]),
(iGalley,					lMaghrebGalleyNames,[iSunni, iShia],			set([rRhodes, rLowerEgypt, rCyprus, rPalestine, rLebanon, rThrace, rCilicia, rLycia, rAsia, rNorthernSyria, rLibya])),
(iGalley,					lGalleyNames,		[iCatholicism, iOrthodoxy],	set([rRhodes, rLowerEgypt, rCyprus, rPalestine, rLebanon, rThrace, rCilicia, rLycia, rAsia, rTrebizond, rNorthernSyria, rLibya, Thessaly, rCentralGreece, rMorea, rSerbia, rEpirus, rCrete, rCephalonia])),
(iWarGalley,				lGalleyNames,		[iCatholicism, iOrthodoxy],	set([rRhodes, rLowerEgypt, rCyprus, rPalestine, rLebanon, rThrace, rCilicia, rLycia, rAsia, rTrebizond, rNorthernSyria, rLibya, Thessaly, rCentralGreece, rMorea, rSerbia, rEpirus, rCrete, rCephalonia])),
(iRoundship, 				lGalleyNames,		[iCatholicism, iOrthodoxy],	set([rRhodes, rLowerEgypt, rCyprus, rPalestine, rLebanon, rThrace, rCilicia, rLycia, rAsia, rTrebizond, rNorthernSyria, rLibya, Thessaly, rCentralGreece, rMorea, rSerbia, rEpirus, rCrete, rCephalonia])),
(iDhow,						lDhowNames,			[iSunni, iShia, iHinduism],	set([rHejaz, rBahrain, rOman, rHadhramaut, rJordan, rMerebMellash, rMahra, rYemen, rSindh])),
(iBaghlah,					lDhowNames,			[iSunni, iShia, iHinduism],	set([rHejaz, rBahrain, rOman, rHadhramaut, rJordan, rMerebMellash, rMahra, rYemen, rSindh])),
)

# Mercenary promotion blacklist
mercenaryPromotionBlacklist = {
	iZanjiSwordsman			: (iWoodsman1, iWoodsman2, iWoodsman3, iDrill1, iDrill2, iDrill3, iDrill4),
	iZanjiSpearman		    : (iWoodsman1, iWoodsman2, iWoodsman3, iDrill1, iDrill2, iDrill3, iDrill4),
	iArquebusier_African	: (iWoodsman1, iWoodsman2, iWoodsman3, iGuerilla1, iGuerilla2, iGuerilla3),
	iNaffatun			    : (iWoodsman1, iWoodsman2, iWoodsman3, iAmphibious, iMedic1, iMedic2),
	iVarangianGuard		    : (iWoodsman1, iWoodsman2, iWoodsman3, iGuerilla1, iGuerilla2, iGuerilla3, iMedic1, iMedic2, iDrill1, iDrill2, iDrill3, iDrill4),
	iJavelinman_African	    : (iWoodsman1, iWoodsman2, iWoodsman3),
	iArcher_African		    : (iWoodsman1, iWoodsman2, iWoodsman3),
	iSpearman_African	    : (iWoodsman1, iWoodsman2, iWoodsman3),
	iArquebusier_African	: (iWoodsman1, iWoodsman2, iWoodsman3),
	iManAtArms				: (iWoodsman1, iWoodsman2, iWoodsman3, iGuerilla1, iGuerilla2, iGuerilla3, iDrill1, iDrill2, iDrill3, iDrill4),
	iArcher_Bedouin			: (iWoodsman1, iWoodsman2, iWoodsman3, iAmphibious),
	iSpearman_Bedouin		: (iWoodsman1, iWoodsman2, iWoodsman3, iAmphibious),
	iArquebusier_Bedouin	: (iWoodsman1, iWoodsman2, iWoodsman3, iAmphibious),
	iMusketman_Bedouin		: (iWoodsman1, iWoodsman2, iWoodsman3, iAmphibious),
	iPashtunWarrior			: (iAmphibious, ),
	iPashtunCavalry			: (iAmphibious, ),
	iAfghanInfantry			: (iAmphibious, ),
	iAfghanPikeman			: (iAmphibious, ),
	iDaylamiTribesman		: (iAmphibious, ),
	iDaylamiInfantry		: (iAmphibious, ),
	iSwordsman_Kipchak		: (iAmphibious, ),
	iHeavySwordsman_Rajput	: (iAmphibious, ),
	iHeavySwordsman_Afghan	: (iAmphibious, ),
	iWarElephant			: (iSkirmish, iMobility, iBlitz, iSentry, iFlanking1, iFlanking2, iFlanking3),
	iHeavyWarElephant		: (iSkirmish, iMobility, iBlitz, iSentry, iFlanking1, iFlanking2, iFlanking3),
}

# Mercenary promotion odds
mercenaryPromotionOdds = {
	iCombat1 : 100,
	iCombat2 : 80,
	iCombat3 : 60,
	iCombat4 : 40,
	iCombat5 : 20,
	iCombat6 : 0,
	iCover : 50,
	iShock : 50,
	iPinch : 50,
	iFormation : 50,
	iSkirmish : 50,
	iCharge : 50,
	iAmphibious : 20,
	iMarch : 20,
	iBlitz : 10,
	iCommando : 0,
	iMedic1 : 0,
	iMedic2 : 0,
	iMedic3 : 0,
	iGuerilla1 : 80,
	iGuerilla2 : 60,
	iGuerilla3 : 40,
	iWoodsman1 : 80,
	iWoodsman2 : 60,
	iWoodsman3 : 40,
	iCityRaider1 : 100,
	iCityRaider2 : 80,
	iCityRaider3 : 60,
	iCityGarrison1 : 100,
	iCityGarrison2 : 80,
	iCityGarrison3 : 60,
	iDrill1 : 100,
	iDrill2 : 80,
	iDrill3 : 60,
	iDrill4 : 40,
	iBarrage1 : 80,
	iBarrage2 : 60,
	iBarrage3 : 40,
	iAccuracy : 40,
	iFlanking1 : 100,
	iFlanking2 : 80,
	iFlanking3 : 60,
	iSentry : 20,
	iMobility : 50,
	iNavigation1 : 80,
	iNavigation2 : 60,
	iLeader : 0,
	iLeadership : 0,
	iTactics : 0,
	iMorale : 0,
	iFeintAttack : 10,
	iEncirclement : 0,
	iGreekFire : 0,
	iDesertAdaptation : 0,
	iBlessed : 0,
	iRaider : 0,
	iMercenary : 0,
	# all remaining promotions : 0%
}