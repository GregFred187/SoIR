# Rhye's and Fall of Civilization - Stored Data

# Moved all read/write functions here so that pickling is only done on load & preSave - edead

from CvPythonExtensions import *
import CvUtil
import cPickle as pickle
from Consts import iNumPlayers
from random import shuffle

# globals
gc = CyGlobalContext()


class StoredData:


	def __init__(self):
		self.setup()

	def setup(self):
		
		self.scriptDict = {
				#------------RiseAndFall
				'iNewCiv': -1,
				'iNewCivFlip': -1,
				'iOldCivFlip': -1,
				'iSpawnWar': 0, #if 1, add units and declare war. If >=2, do nothing
				'bAlreadySwitched': False,
				'lNumCities':			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #total players to contain Byzantium too
				'lLastTurnAlive':		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #total players to contain Byzantium too
				'lSpawnDelay':			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #active players
				'lFlipsDelay':			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'iBetrayalTurns': 0,
				'lLatestRebellionTurn': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'iRebelCiv': 0,
				'lExileData': [-1, -1, -1, -1, -1],
				'tTempFlippingCity': -1,
				'lCheatersCheck': [0, -1],
				# 'lBirthTurnModifier': 	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'lDeleteMode': [-1, -1, -1], #first is a bool, the other values are capital coordinates
				'bCheatMode': False,
				#------------AIWars
				'lAttackingCivsArray': 	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'iNextTurnAIWar': -1,
				#------------Plague
				'lPlagueCountdown': 	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0], #total players + barbarians
				'lGenericPlagueDates': [-1, -1, -1],
				#------------Victories
				'lGoals': [[-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],                       
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],					   
					   [-1, -1, -1],					   
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],					   
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],					   
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],					   
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1]],
				'lReligiousGoals': [[-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],                       
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],					   
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],					   
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],					   
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],					   
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1],
					   [-1, -1, -1]],
				'iRazedByMongols': 0,
				'iNumSinks': 0,
				'iNumConversions': 0,
				'iNumGenerals': 0,
				'iNumSaints': 0,
				'lOttomanTechs': [-1, -1, -1], 
				'lMalwaBuildings': [0, 0],
				'lWondersBuilt': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'l2OutOf3': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
				#------------Stability
				'lBaseStabilityLastTurn': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'lPartialBaseStability': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'lStability': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'lOwnedPlotsLastTurn': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'lOwnedCitiesLastTurn': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'lCombatResultTempModifier': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'lGNPold': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'lGNPnew': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'lStabilityParameters': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #2+3+2+3+3
				'lLastRecordedStabilityStuff': [0, 0, 0, 0, 0, 0], # total + 5 parameters
			   #'iCounter': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'iCounter': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'plotList': [],
				'lCivStatus': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 0: Default, 1: Respawned
				'lStopSpawn': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				#----------Traits/UPs
				'iNumCrusades': 0,
				'lHasLostCity': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
			   #'lLastCrusadeTurn': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'lLastCrusadeTurn': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   
				'iLatestFlipTurn': 0,
				#----------Religions
				'lBasePiety': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				#----------Possibly too high?
				'lPiety': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
				'iLastHolyWarTurn': -101,
				'iHolyWarTarget': -1,
				'lPersecutionData': [-1, -1, -1],
				'lPersecutionReligions': [],
				#----------Misc
				'iSeed': 0,
				'lRandomCivList': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41],
				'lCivilization': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41],
				#----------Mercenaries
				'mercenaryData': {
					"AvailableMercenaries" : {},
					"HiredMercenaries" : {0:{}, 1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}, 8:{}, 9:{}, 10:{}, 11:{}, 12:{}, 13:{}, 14:{}, 15:{}, 16:{}, 17:{}, 18:{}, 19:{}, 20:{}, 21:{}, 22:{}, 23:{}, 24:{}, 25:{}, 26:{}, 27:{}, 28:{}, 29:{}, 30:{}, 31:{}, 32:{}, 33:{}, 34:{}, 35:{}, 36:{}, 37:{}, 38:{}, 39:{}, 40:{}, 41:{}, 42:{}, 43:{}, 44:{}, 45:{}, 46:{}, 47:{}},
					"MercenaryGroups" : {},
					"MercenaryNames" : {},
					"UnplacedMercenaries" : {},
					},
			}
		
		self.setSeed()
		self.setRandomCivList()

	def load(self):
		'Loads and unpickles script data'
		self.scriptDict = pickle.loads(gc.getGame().getScriptData())

	def save(self):
		'Pickles and saves script data'
		gc.getGame().setScriptData(pickle.dumps(self.scriptDict))

	# from Stability.py

	def getStability( self, iCiv ):
		if iCiv >= iNumPlayers: return 0
		return self.scriptDict['lStability'][iCiv]

	def setStability( self, iCiv, iNewValue ):
		self.scriptDict['lStability'][iCiv] = iNewValue

	def getBaseStabilityLastTurn( self, iCiv ):
		return self.scriptDict['lBaseStabilityLastTurn'][iCiv]

	def setBaseStabilityLastTurn( self, iCiv, iNewValue ):
		self.scriptDict['lBaseStabilityLastTurn'][iCiv] = iNewValue

	def getCombatResultTempModifier( self, iCiv ):
		return self.scriptDict['lCombatResultTempModifier'][iCiv]

	def setCombatResultTempModifier( self, iCiv, iNewValue ):
		self.scriptDict['lCombatResultTempModifier'][iCiv] = iNewValue

	def getGNPold( self, iCiv ):
		return self.scriptDict['lGNPold'][iCiv]

	def setGNPold( self, iCiv, iNewValue ):
		self.scriptDict['lGNPold'][iCiv] = iNewValue

	def getGNPnew( self, iCiv ):
		return self.scriptDict['lGNPnew'][iCiv]

	def setGNPnew( self, iCiv, iNewValue ):
		self.scriptDict['lGNPnew'][iCiv] = iNewValue

	def getLatestRebellionTurn( self, iCiv ):
		return self.scriptDict['lLatestRebellionTurn'][iCiv]

	def getPartialBaseStability( self, iCiv ):
		return self.scriptDict['lPartialBaseStability'][iCiv]

	def setPartialBaseStability( self, iCiv, iNewValue ):
		self.scriptDict['lPartialBaseStability'][iCiv] = iNewValue

	def getOwnedPlotsLastTurn( self, iCiv ):
		return self.scriptDict['lOwnedPlotsLastTurn'][iCiv]

	def setOwnedPlotsLastTurn( self, iCiv, iNewValue ):
		self.scriptDict['lOwnedPlotsLastTurn'][iCiv] = iNewValue

	def getOwnedCitiesLastTurn( self, iCiv ):
		return self.scriptDict['lOwnedCitiesLastTurn'][iCiv]

	def setOwnedCitiesLastTurn( self, iCiv, iNewValue ):
		self.scriptDict['lOwnedCitiesLastTurn'][iCiv] = iNewValue

	def getStabilityParameters( self, iParameter ):
		return self.scriptDict['lStabilityParameters'][iParameter]

	def setStabilityParameters( self, iParameter, iNewValue ):
		self.scriptDict['lStabilityParameters'][iParameter] = iNewValue

	def getLastRecordedStabilityStuff( self, iParameter ):
		return self.scriptDict['lLastRecordedStabilityStuff'][iParameter]

	def setLastRecordedStabilityStuff( self, iParameter, iNewValue ):
		self.scriptDict['lLastRecordedStabilityStuff'][iParameter] = iNewValue

	# from RiseAndFall.py

	def getNewCiv( self ):
		return self.scriptDict['iNewCiv']

	def setNewCiv( self, iNewValue ):
		self.scriptDict['iNewCiv'] = iNewValue

	def getNewCivFlip( self ):
		return self.scriptDict['iNewCivFlip']

	def setNewCivFlip( self, iNewValue ):
		self.scriptDict['iNewCivFlip'] = iNewValue

	def getOldCivFlip( self ):
		return self.scriptDict['iOldCivFlip']

	def setOldCivFlip( self, iNewValue ):
		self.scriptDict['iOldCivFlip'] = iNewValue

	def getSpawnWar( self ):
		return self.scriptDict['iSpawnWar']

	def setSpawnWar( self, iNewValue ):
		self.scriptDict['iSpawnWar'] = iNewValue

	def getAlreadySwitched( self ):
		return self.scriptDict['bAlreadySwitched']

	def setAlreadySwitched( self, bNewValue ):
		self.scriptDict['bAlreadySwitched'] = bNewValue

	def getNumCities( self, iCiv ):
		return self.scriptDict['lNumCities'][iCiv]

	def setNumCities( self, iCiv, iNewValue ):
		self.scriptDict['lNumCities'][iCiv] = iNewValue

	def getSpawnDelay( self, iCiv ):
		return self.scriptDict['lSpawnDelay'][iCiv]

	def setSpawnDelay( self, iCiv, iNewValue ):
		self.scriptDict['lSpawnDelay'][iCiv] = iNewValue

	def getFlipsDelay( self, iCiv ):
		return self.scriptDict['lFlipsDelay'][iCiv]

	def setFlipsDelay( self, iCiv, iNewValue ):
		self.scriptDict['lFlipsDelay'][iCiv] = iNewValue

	def getBetrayalTurns( self ):
		return self.scriptDict['iBetrayalTurns']

	def setBetrayalTurns( self, iNewValue ):
		self.scriptDict['iBetrayalTurns'] = iNewValue

	def getLatestFlipTurn( self ):
		return self.scriptDict['iLatestFlipTurn']

	def setLatestFlipTurn( self, iNewValue ):
		self.scriptDict['iLatestFlipTurn'] = iNewValue

	def getLatestRebellionTurn( self, iCiv ):
		return self.scriptDict['lLatestRebellionTurn'][iCiv]

	def setLatestRebellionTurn( self, iCiv, iNewValue ):
		self.scriptDict['lLatestRebellionTurn'][iCiv] = iNewValue

	def getRebelCiv( self ):
		return self.scriptDict['iRebelCiv']

	def setRebelCiv( self, iNewValue ):
		self.scriptDict['iRebelCiv'] = iNewValue

	def getExileData( self, i ):
		return self.scriptDict['lExileData'][i]

	def setExileData( self, i, iNewValue ):
		self.scriptDict['lExileData'][i] = iNewValue

	def getTempFlippingCity( self ):
		return self.scriptDict['tempFlippingCity']

	def setTempFlippingCity( self, tNewValue ):
		self.scriptDict['tempFlippingCity'] = tNewValue

	def getCheatersCheck( self, i ):
		return self.scriptDict['lCheatersCheck'][i]

	def setCheatersCheck( self, i, iNewValue ):
		self.scriptDict['lCheatersCheck'][i] = iNewValue

	def getDeleteMode( self, i ):
		return self.scriptDict['lDeleteMode'][i]

	def setDeleteMode( self, i, iNewValue ):
		self.scriptDict['lDeleteMode'][i] = iNewValue

	def getCheatMode( self ):
		return self.scriptDict['bCheatMode']

	def setCheatMode( self, bNewValue ):
		self.scriptDict['bCheatMode'] = bNewValue

	def setCounter(self, iCounterID, iNewValue):
		self.scriptDict['iCounter'][iCounterID] = iNewValue

	def getCounter( self, iCounterID ):
		return self.scriptDict['iCounter'][iCounterID]

	def setTempPlotList( self, lNewList ):
		self.scriptDict['plotList'] = lNewList

	def getTempPlotList( self ):
		return self.scriptDict['plotList']

	def setStopSpawn(self, iCiv, iNewValue):
		self.scriptDict['lStopSpawn'][iCiv] = iNewValue

	def getStopSpawn( self, iCiv ):
		return self.scriptDict['lStopSpawn'][iCiv]

	# from Victory.py
	
	def getGoal( self, i, j ):
		return self.scriptDict['lGoals'][i][j]

	def setGoal( self, i, j, iNewValue ):
		self.scriptDict['lGoals'][i][j] = iNewValue
	
	def getReligiousGoal( self, i, j ):
		return self.scriptDict['lReligiousGoals'][i][j]

	def setReligiousGoal( self, i, j, iNewValue ):
		self.scriptDict['lReligiousGoals'][i][j] = iNewValue

	def getRazedByMongols( self ):
		return self.scriptDict['iRazedByMongols']

	def setRazedByMongols( self, iNewValue ):
		self.scriptDict['iRazedByMongols'] = iNewValue

	def getWondersBuilt( self, iCiv ):
		return self.scriptDict['lWondersBuilt'][iCiv]

	def setWondersBuilt( self, iCiv, iNewValue ):
		self.scriptDict['lWondersBuilt'][iCiv] = iNewValue

	def getOttomanTechs( self, i ):
		return self.scriptDict['lOttomanTechs'][i]

	def setOttomanTechs( self, i, iNewValue ):
		self.scriptDict['lOttomanTechs'][i] = iNewValue

	def getNumSinks( self ):
		return self.scriptDict['iNumSinks']

	def setNumSinks( self, iNewValue ):
		self.scriptDict['iNumSinks'] = iNewValue

	def getNumConversions( self ):
		return self.scriptDict['iNumConversions']

	def setNumConversions( self, iNewValue ):
		self.scriptDict['iNumConversions'] = iNewValue

	def getNumGenerals( self ):
		return self.scriptDict['iNumGenerals']

	def setNumGenerals( self, iNewValue ):
		self.scriptDict['iNumGenerals'] = iNewValue

	def get2OutOf3( self, iCiv ):
		return self.scriptDict['l2OutOf3'][iCiv]

	def set2OutOf3( self, iCiv, bNewValue ):
		self.scriptDict['l2OutOf3'][iCiv] = bNewValue

	# from RFCUtils.py

	def getCivilization(self, iCiv):
		return self.scriptDict['lCivilization'][iCiv]

	def getLastTurnAlive( self, iCiv ):
		return self.scriptDict['lLastTurnAlive'][iCiv]

	def setLastTurnAlive( self, iCiv, iNewValue ):
		self.scriptDict['lLastTurnAlive'][iCiv] = iNewValue

	def getCivStatus(self, iCiv):
		return self.scriptDict['lCivStatus'][iCiv]

	def setCivStatus(self, iCiv, iNewValue):
		self.scriptDict['lCivStatus'][iCiv] = iNewValue

	def getNumCrusades(self):
		return self.scriptDict['iNumCrusades']

	def setNumCrusades(self, iNewValue):
		self.scriptDict['iNumCrusades'] = iNewValue

	def isHasLostCity(self, iCiv):
		return self.scriptDict['lHasLostCity'][iCiv]

	def setHasLostCity(self, iCiv, iNewValue):
		self.scriptDict['lHasLostCity'][iCiv] = iNewValue

	def getLastCrusadeTurn(self, iCiv):
		return self.scriptDict['lLastCrusadeTurn'][iCiv]

	def setLastCrusadeTurn(self, iCiv, iNewValue):
		self.scriptDict['lLastCrusadeTurn'][iCiv] = iNewValue

	# from Plague.py

	def getGenericPlagueDates( self, i ):
		return self.scriptDict['lGenericPlagueDates'][i]

	def setGenericPlagueDates( self, i, iNewValue ):
		self.scriptDict['lGenericPlagueDates'][i] = iNewValue

	def getPlagueCountdown( self, iCiv ):
		return self.scriptDict['lPlagueCountdown'][iCiv]

	def setPlagueCountdown( self, iCiv, iNewValue ):
		self.scriptDict['lPlagueCountdown'][iCiv] = iNewValue

	# from Religions.py

	def getBasePiety(self, iCiv):
		return self.scriptDict['lBasePiety'][iCiv]

	def setBasePiety(self, iCiv, iNewValue):
		self.scriptDict['lBasePiety'][iCiv] = max(0, min(100, iNewValue))

	def changePiety(self, iCiv, iChange):
		iNewValue = self.getPiety(iCiv) + iChange
		self.scriptDict['lPiety'][iCiv] = max(0, min(100, iNewValue))
		
	def getPiety(self, iCiv):
		if iCiv >= iNumPlayers: return -1
		return self.scriptDict['lPiety'][iCiv]

	def setPiety(self, iCiv, iNewValue):
		self.scriptDict['lPiety'][iCiv] = max(0, min(100, iNewValue))

	def getPersecutionData(self):
		return self.scriptDict['lPersecutionData'][0], self.scriptDict['lPersecutionData'][1], self.scriptDict['lPersecutionData'][2]

	def setPersecutionData(self, iX, iY, iID):
		self.scriptDict['lPersecutionData'] = [iX, iY, iID]

	def getPersecutionReligions(self):
		return self.scriptDict['lPersecutionReligions']

	def setPersecutionReligions(self, val):
		self.scriptDict['lPersecutionReligions'] = val

	# from AIWars.py

	def getAttackingCivsArray( self, iCiv ):
		return self.scriptDict['lAttackingCivsArray'][iCiv]

	def setAttackingCivsArray( self, iCiv, iNewValue ):
		self.scriptDict['lAttackingCivsArray'][iCiv] = iNewValue

	def getNextTurnAIWar( self ):
		return self.scriptDict['iNextTurnAIWar']

	def setNextTurnAIWar( self, iNewValue ):
		self.scriptDict['iNextTurnAIWar'] = iNewValue

	# Mercenaries

	def getMercenaryData(self, key):
		return self.scriptDict['mercenaryData'][key]

	def setMercenaryData(self, key, value):
		self.scriptDict['mercenaryData'][key] = value
	
	# Misc
	
	def getSeed( self ):
		return self.scriptDict['iSeed']

	def setSeed( self ):
		self.scriptDict['iSeed'] = gc.getGame().getSorenRandNum(100, 'Seed for random delay')
	
	def getRandomCivList( self ):
		return self.scriptDict['lRandomCivList']

	def setRandomCivList( self ):
		shuffle(self.scriptDict['lRandomCivList'])
	
	# Generic
	
	def getVal( self, sVal ):
		if sVal in self.scriptDict:
			return self.scriptDict[sVal]
		
	def setVal( self, sVal, iNewValue ):
		self.scriptDict[sVal] = iNewValue

	def delVal( self, sVal ):
		del self.scriptDict[sVal]

# All modules import the following single instance, not the class

sd = StoredData()