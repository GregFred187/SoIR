# Rhye's and Fall of Civilization - AI Wars

from CvPythonExtensions import *
import CvUtil
import PyHelpers
import Popup
import Consts as con
from StoredData import sd
from RFCUtils import utils

# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer

### Constants ###

iStartTurn = 20
iMinInterval = 20
iMaxInterval = 40
iThreshold = 100
iMinValue = 30
iNumPlayers = con.iNumPlayers
iIndependent = con.iIndependent
iIndependent2 = con.iIndependent2
iIndependent3 = con.iIndependent3
iIndependent4 = con.iIndependent4
iNumTotalPlayers = con.iBarbarian

  
class AIWars:


	def setup(self):
		iTurn = utils.getTurns(iStartTurn + gc.getGame().getSorenRandNum(iMaxInterval-iMinInterval, 'random turn'))
		sd.setNextTurnAIWar(iTurn)

	def checkTurn(self, iGameTurn):
		
		#turn automatically peace on between independent cities and all the major civs
		if (iGameTurn % 20 == 0):
			utils.restorePeaceHuman(iIndependent4, False)
		if (iGameTurn % 20 == 5):
			utils.restorePeaceHuman(iIndependent3, False)
		if (iGameTurn % 20 == 10):
			utils.restorePeaceHuman(iIndependent2, False)
		if (iGameTurn % 20 == 20):
			utils.restorePeaceHuman(iIndependent, False)
		
		if (iGameTurn % 20 == 1 and iGameTurn > 40):
			utils.restorePeaceAI(iIndependent, False)
		if (iGameTurn % 20 == 6 and iGameTurn > 40):
			utils.restorePeaceAI(iIndependent2, False)
		if (iGameTurn % 20 == 11 and iGameTurn > 40):
			utils.restorePeaceAI(iIndependent3, False)
		if (iGameTurn % 20 == 16 and iGameTurn > 40):
			utils.restorePeaceAI(iIndependent4, False)
		
		#turn automatically war on between independent cities and some AI major civs
		if (iGameTurn % 20 == 2 and iGameTurn > 40): #1 turn after restorePeace()
			utils.minorWars(iIndependent)
		if (iGameTurn % 20 == 7 and iGameTurn > 40): #1 turn after restorePeace()
			utils.minorWars(iIndependent2)
		if (iGameTurn % 20 == 12 and iGameTurn > 40): #1 turn after restorePeace()
			utils.minorWars(iIndependent3)
		if (iGameTurn % 20 == 17 and iGameTurn > 40): #1 turn after restorePeace()
			utils.minorWars(iIndependent4)
		
		if (iGameTurn == sd.getNextTurnAIWar()):
			
			iCiv, iTargetCiv = self.pickCivs()
			if (iTargetCiv >= 0 and iTargetCiv <= iNumTotalPlayers):
				self.initWar(iCiv, iTargetCiv, iGameTurn, iMaxInterval, iMinInterval)
				return
			else:
				print ("AIWars iTargetCiv missing", iCiv)
				iCiv, iTargetCiv = self.pickCivs()
				if (iTargetCiv >= 0 and iTargetCiv <= iNumTotalPlayers):
					self.initWar(iCiv, iTargetCiv, iGameTurn, iMaxInterval, iMinInterval)
					return
				else:
					print ("AIWars iTargetCiv missing again", iCiv)

			#make sure we don't miss this
			print("Skipping AIWar")
			sd.setNextTurnAIWar(iGameTurn + iMinInterval + gc.getGame().getSorenRandNum(iMaxInterval-iMinInterval, 'random turn'))


	def pickCivs(self): 
		iCiv = -1
		iTargetCiv = -1
		iCiv = self.chooseAttackingPlayer()
		if iCiv >= 0 and iCiv < iNumPlayers:
			iTargetCiv = self.checkGrid(iCiv)
			return (iCiv, iTargetCiv)
		else:
			print ("AIWars iCiv missing", iCiv)
			return (-1, -1)

	def initWar(self, iCiv, iTargetCiv, iGameTurn, iMaxInterval, iMinInterval): 
		
		# edead: instead of declaring war, start war preparations; declare immediately if indeps are involved
		if iTargetCiv < iNumPlayers:
			gc.getTeam(gc.getPlayer(iCiv).getTeam()).AI_setWarPlan(iTargetCiv, WarPlanTypes.WARPLAN_PREPARING_LIMITED)
		else:
			gc.getTeam(gc.getPlayer(iCiv).getTeam()).declareWar(iTargetCiv, True, -1)
		
		sd.setNextTurnAIWar(iGameTurn + iMinInterval + gc.getGame().getSorenRandNum(iMaxInterval-iMinInterval, 'random turn'))
		print("Setting AIWar", iCiv, "attacking", iTargetCiv)


	def chooseAttackingPlayer(self): 
		#finding max teams ever alive (countCivTeamsEverAlive() doesn't work as late human starting civ gets killed every turn)
		iMaxCivs = iNumPlayers
		for i in range( iNumPlayers ):
			j = iNumPlayers -1 - i
			if (gc.getPlayer(j).isAlive()):
				iMaxCivs = j
				break 
		#print ("iMaxCivs", iMaxCivs)
		
		if (gc.getGame().countCivPlayersAlive() <= 3):
			return -1
		else:
			iRndnum = gc.getGame().getSorenRandNum(iMaxCivs, 'attacking civ index') 
			
			# Important war: Ottomans vs. Karaman
			if utils.getYear() >= 1400 and utils.getYear() < 1500:
				if gc.getPlayer(con.iRum).isAlive() and gc.getPlayer(con.iOttomans).isAlive():
					if not gc.getTeam(gc.getPlayer(con.iRum).getTeam()).isAtWar(con.iOttomans):
						if gc.getPlayer(con.iRum) != utils.getHumanID():
							iRndnum = con.iRum
						elif gc.getPlayer(con.iOttomans) != utils.getHumanID():
							iRndnum = con.iOttomans
			
			#print ("iRndnum", iRndnum)
			iAlreadyAttacked = -100
			iMin = 100
			iCiv = -1
			for i in range( iRndnum, iRndnum + iMaxCivs ):
				iLoopCiv = i % iMaxCivs
				pLoopPlayer = gc.getPlayer(iLoopCiv)
				if (pLoopPlayer.isAlive() and not pLoopPlayer.isHuman()):
					if (sd.getPlagueCountdown(iLoopCiv) >= -10 and sd.getPlagueCountdown(iLoopCiv) <= 0): #civ is not under plague or quit recently from it
						iAlreadyAttacked = sd.getAttackingCivsArray(iLoopCiv)
						if (utils.isAVassal(iLoopCiv)):
							iAlreadyAttacked += 1 #less likely to attack
						#check if a world war is already in place
						iNumAlreadyWar = 0
						tLoopCiv = gc.getTeam(pLoopPlayer.getTeam())
						for kLoopCiv in range( iNumPlayers ):
							if (tLoopCiv.isAtWar(kLoopCiv)):
								if gc.getPlayer(kLoopCiv).isAlive():
									iNumAlreadyWar += 1
						if (iNumAlreadyWar >= 4):
							iAlreadyAttacked += 2 #much less likely to attack
						elif (iNumAlreadyWar >= 2):
							iAlreadyAttacked += 1 #less likely to attack
						
						if (iAlreadyAttacked < iMin):
							iMin = iAlreadyAttacked
							iCiv = iLoopCiv
				#print ("attacking civ", iCiv)
				if (iAlreadyAttacked != -100):
					sd.setAttackingCivsArray(iCiv, iAlreadyAttacked + 1)
					return iCiv
				else:
					return -1
		return -1


	def checkGrid(self, iCiv):
		
		pCiv = gc.getPlayer(iCiv)
		tCiv = gc.getTeam(pCiv.getTeam())
		lTargetCivs = []

		#clean it, sometimes it takes old values in memory
		for k in range(iNumTotalPlayers):
			lTargetCivs.append(0)

		#set alive civs to 1 to differentiate them from dead civs
		for k in range(iNumTotalPlayers):
			if gc.getPlayer(k).isAlive() and tCiv.isHasMet(k):
				lTargetCivs[k] = 1

		#set master or vassal to 0
		for k in range(iNumPlayers):
			if gc.getTeam(gc.getPlayer(k).getTeam()).isVassal(iCiv) or tCiv.isVassal(k):
				lTargetCivs[k] = 0

		#if already at war
		for k in range(iNumTotalPlayers): 
			if tCiv.isAtWar(k):
				lTargetCivs[k] = 0

		lTargetCivs[iCiv] = 0
		
		#edead: changed Rhye's code to Regions (provinces)
		map = CyMap()
		for i in range(map.numPlots()):
			plot = map.plotByIndex(i)
			if plot.isCity():
				iOwner = plot.getOwner()
				if iOwner >= 0 and iOwner < iNumTotalPlayers and iOwner != iCiv:
					if lTargetCivs[iOwner] > 0:
						regionID = plot.getRegionID()
						if regionID in utils.getCoreRegions(iCiv): 
							lTargetCivs[iOwner] += 10
						elif regionID in utils.getNormalRegions(iCiv): 
							lTargetCivs[iOwner] += 5
						elif regionID in utils.getBroaderRegions(iCiv): 
							lTargetCivs[iOwner] += 2
		
		#edead: otherwise they'll just kill each other
		if iCiv == con.iAntioch:
			lTargetCivs[con.iCrusaders] = 0
		elif iCiv == con.iCrusaders:
			lTargetCivs[con.iAntioch] = 0
		
		#edead: important war
		if utils.getYear() >= 1400 and utils.getYear() < 1500:
			if iCiv == con.iOttomans:
				lTargetCivs[con.iRum] += 30
			elif iCiv == con.iRum:
				lTargetCivs[con.iOttomans] += 30
		
		#there are other routines for this
		lTargetCivs[iIndependent] /= 3
		lTargetCivs[iIndependent2] /= 3
		lTargetCivs[iIndependent3] /= 3
		lTargetCivs[iIndependent4] /= 3
		
		#no random silly wars - edead
		for k in range(iNumTotalPlayers):
			if lTargetCivs[k] == 1:
				lTargetCivs[k] = 0
		
		print("AIWars grid for ", iCiv)
		print(lTargetCivs)
		
		#normalization
		iMaxTempValue = -1
		for k in range( iNumTotalPlayers ):
			if (lTargetCivs[k] > iMaxTempValue):
				iMaxTempValue = lTargetCivs[k]
		if (iMaxTempValue > 0):
			for k in range( iNumTotalPlayers ):
				if (lTargetCivs[k] > 0):
					lTargetCivs[k] = lTargetCivs[k]*500/iMaxTempValue
			
		print(lTargetCivs)
		
		for iLoopCiv in range( iNumTotalPlayers ):
		
			if (lTargetCivs[iLoopCiv] <= 0):
				continue
				
			#add a random value
			if (lTargetCivs[iLoopCiv] <= iThreshold):
				lTargetCivs[iLoopCiv] += gc.getGame().getSorenRandNum(100, 'random modifier')
			if (lTargetCivs[iLoopCiv] > iThreshold):
				lTargetCivs[iLoopCiv] += gc.getGame().getSorenRandNum(300, 'random modifier')
			
			#balanced with attitude
			attitude = 2*(pCiv.AI_getAttitude(iLoopCiv) - 2)
			if (attitude > 0):
				lTargetCivs[iLoopCiv] /= attitude
			
			#exploit plague
			if iLoopCiv < iNumPlayers:
				if (sd.getPlagueCountdown(iLoopCiv) > 0 or sd.getPlagueCountdown(iLoopCiv) < -10 and not (gc.getGame().getGameTurn() <= getTurnForYear(con.tBirth[iLoopCiv]) + utils.getTurns(20))):
					lTargetCivs[iLoopCiv] *= 3
					lTargetCivs[iLoopCiv] /= 2
			
			#balanced with master's attitude
			for j in range( iNumTotalPlayers ):
				if (tCiv.isVassal(j)):
					attitude = 2*(gc.getPlayer(j).AI_getAttitude(iLoopCiv) - 2)
					if (attitude > 0):
						lTargetCivs[iLoopCiv] /= attitude
			
			#if already at war 
			if (not tCiv.isAtWar(iLoopCiv)):
				#consider peace counter
				iCounter = min(7,max(1,tCiv.AI_getAtPeaceCounter(iLoopCiv)))
				if (iCounter <= 7):
					lTargetCivs[iLoopCiv] *= 20 + 10*iCounter
					lTargetCivs[iLoopCiv] /= 100
				
			#if under pact
			if (tCiv.isDefensivePact(iLoopCiv)):
				lTargetCivs[iLoopCiv] /= 4
			
			#if friend of a friend
##					for jLoopCiv in range( iNumTotalPlayers ):
##						if (tCiv.isDefensivePact(jLoopCiv) and gc.getTeam(gc.getPlayer(iLoopCiv).getTeam()).isDefensivePact(jLoopCiv)):
##							lTargetCivs[iLoopCiv] /= 2
			
		print(lTargetCivs)
		
		#find max
		iMaxValue = 0
		iTargetCiv = -1
		for iLoopCiv in range( iNumTotalPlayers ):
			if (lTargetCivs[iLoopCiv] > iMaxValue):
				iMaxValue = lTargetCivs[iLoopCiv]
				iTargetCiv = iLoopCiv

		print("maxvalue", iMaxValue)
		print("target civ", iTargetCiv)

		if (iMaxValue >= iMinValue):
			return iTargetCiv
		return -1

