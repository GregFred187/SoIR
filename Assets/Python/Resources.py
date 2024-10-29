# Dynamic resources - based on Rhye's and Fall of Civilizations
# rewritten by edead

from CvPythonExtensions import *
import CvUtil
import Consts as con
from StoredData import sd
from RFCUtils import utils

# globals
gc = CyGlobalContext()
localText = CyTranslator()


class Resources:


	def createResource(self, iX, iY, iBonus, textKey="TXT_KEY_MISC_DISCOVERED_NEW_RESOURCE"):
		"""Creates a bonus resource and alerts the plot owner"""
		
		if gc.getMap().plot(iX,iY).getBonusType(-1) == -1 or iBonus == -1: # only proceed if the bonus isn't already there or if we're removing the bonus
			if iBonus == -1:
				iBonus = gc.getMap().plot(iX,iY).getBonusType(-1) # for alert
				gc.getMap().plot(iX,iY).setBonusType(-1)
			else:
				gc.getMap().plot(iX,iY).setBonusType(iBonus)
				
			iOwner = gc.getMap().plot(iX,iY).getOwner()
			if iOwner >= 0 and textKey != -1: # only show alert to the tile owner
				city = gc.getMap().findCity(iX, iY, iOwner, TeamTypes.NO_TEAM, True, False, TeamTypes.NO_TEAM, DirectionTypes.NO_DIRECTION, CyCity())
				if not city.isNone():
					szText = localText.getText(textKey, (gc.getBonusInfo(iBonus).getTextKey(), city.getName(), gc.getPlayer(iOwner).getCivilizationAdjective(0)))
					CyInterface().addMessage(iOwner, False, con.iDuration, szText, "AS2D_DISCOVERBONUS", InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, gc.getBonusInfo(iBonus).getButton(), ColorTypes(con.iWhite), iX, iY, True, True)


	def removeResource(self, iX, iY, textKey="TXT_KEY_MISC_EVENT_RESOURCE_EXHAUSTED"):
		"""Removes a bonus resource and alerts the plot owner"""
		
		self.createResource(iX, iY, -1, textKey)


	def checkTurn(self, iGameTurn):
		
		if iGameTurn == getTurnForYear(760) and utils.getHumanID() != con.iAbbasids:
			#gc.getMap().plot(52, 40).setImprovementType(13) # quarry near Baghdad to encourage wonders
			gc.getMap().plot(52, 42).setImprovementType(7) # mine near Baghdad to encourage wonders
		
		if iGameTurn == getTurnForYear(820) and utils.getHumanID() != con.iAbbasids:
			gc.getMap().plot(51, 45).setImprovementType(7) # mine near Samarra to encourage wonders
		
		if iGameTurn == getTurnForYear(1070): 
			self.createResource(29, 53, con.iHorse) # Konya/Karaman
			self.createResource(29, 55, con.iCow) # Konya/Karaman
			
		if iGameTurn == getTurnForYear(1075)-1:
			self.createResource(82, 63, con.iHorse) # Khiva
			self.createResource(82, 65, con.iCow) # Urgench
		
		if iGameTurn == getTurnForYear(1099): 
			self.createResource(34, 38, con.iHorse) # Acre
		
		if iGameTurn == getTurnForYear(1130): 
			self.createResource(32, 37, con.iCitrus) # Jerusalem
			self.createResource(97, 46, con.iGems) # Kabul
		
		if iGameTurn == getTurnForYear(1140): 
			self.createResource(100, 45, con.iCow) # Peshawar
			self.createResource(112, 33, con.iOpium) # Delhi
			self.createResource(103, 9, con.iCrab) # Bombay
		
		if iGameTurn == getTurnForYear(1200): 
			self.createResource(59, 60, con.iSilk) # Ganja
			self.createResource(110, 34, con.iSugar) # Delhi
			self.createResource(110, 7, con.iSorghum) # Ahsenabad
			
		if iGameTurn == getTurnForYear(1195 + (sd.getSeed() % 10)):
			self.removeResource(35, 42) # Dye near Tyre
			self.removeResource(22, 10) # Barley near Dongola
		
		if iGameTurn == getTurnForYear(1250 + (sd.getSeed() % 20)): 
			self.removeResource(48, 42) # Sugar near Baghdad
			self.removeResource(29, 7) # Dates near Meroe
			if gc.getGame().getSorenRandNum(2, 'Random plot') == 0:
				self.removeResource(32, 34) # Copper near Jerusalem
			else:
				self.removeResource(33, 34) # Salt near Jerusalem

		if iGameTurn == getTurnForYear(1260 + ((sd.getSeed() * 2) % 40)):
			self.removeResource(56, 35) # Rice near Basrah
			self.removeResource(21, 15) # Barley near Faras
				
		if iGameTurn == getTurnForYear(1270 + ((sd.getSeed() / 2) % 10)): 
			self.createResource(59, 56, con.iSilk) # Ardabil
			if gc.getGame().getSorenRandNum(2, 'Random plot') == 0:
				self.removeResource(95, 40) # Silver near Ghazna
				self.removeResource(29, 34) # Olives near Gaza
			else:
				self.removeResource(93, 39) # Silver near Kandahar
				self.removeResource(29, 37) # Fish near Ghazza

		if iGameTurn == getTurnForYear(1299): 
			self.createResource(16, 62, con.iWheat) # Gallipoli
			self.createResource(105,18, con.iRice) # between Khambhat/Surat and Malwa
		
		if iGameTurn == getTurnForYear(1350 + ((sd.getSeed() * 4) % 30)): 
			self.removeResource(22, 11) # Cows near Dongola
			self.removeResource(52, 40) # Stone near Baghdad

		if iGameTurn == getTurnForYear(1350 + ((sd.getSeed() * 3) % 50)):
			if gc.getGame().getSorenRandNum(2, 'Random plot') == 0:
				self.removeResource(24, 32) # Dates near Cairo
			else:
				self.removeResource(24, 30) # Wheat near Cairo
			self.createResource(48, 62, con.iGold) # Kars
			self.createResource(104, 24, con.iSheep) # Jodhpur
			
		if iGameTurn == getTurnForYear(1370 + (sd.getSeed() % 10)):
			self.createResource(56, 54, con.iHorse) # Tabriz
			self.createResource(94, 59, con.iHorse) # Samarkand
			self.createResource(92, 58, con.iCow) # Samarkand
			self.removeResource(28, 20) # Stone near Aswan
		
		if iGameTurn == getTurnForYear(1380):
			self.createResource(93, 56, con.iGold) # Samarkand
			self.createResource(110, 30, con.iMarble) # Agra
			
		if iGameTurn == getTurnForYear(1441):
			self.createResource(32, 73, con.iFish) # Qapi
			self.createResource(35, 74, con.iCow) # Qapi
		
		if iGameTurn == getTurnForYear(1450):
			self.createResource(102, 26, con.iSalt) # Jodhpur

		if iGameTurn == getTurnForYear(1470 + ((sd.getSeed() / 2) % 30)): 
			self.createResource(60, 53, con.iHoney) # Ardabil
			self.removeResource(20, 9) # Copper near Dongola

		if iGameTurn == getTurnForYear(1490): 
			self.createResource(61, 55, con.iFish) # Ardabil
			self.createResource(114, 30, con.iSpices) # Agra
			self.createResource(107, 11, con.iCow) # Ahmadnagar
			self.removeResource(82, 34) # Copper near Zaranj
		
		if iGameTurn == getTurnForYear(1510):
			self.createResource(104, 2, con.iWhale) # Goa
			self.createResource(108, 4, con.iSpices) # Goa
			self.createResource(106, 4, con.iDye) # Goa
			self.removeResource(50, 2) # Copper in Yemen
		
		if iGameTurn == getTurnForYear(1526):
			self.createResource(111, 29, con.iRice) # Agra
			self.createResource(113, 31, con.iCow) # Agra
			self.createResource(63, 41, con.iCopper) # Copper near Isfahan
		
		if iGameTurn == getTurnForYear(1670):
			self.createResource(109, 1, con.iCoffee) # Goa/Karnataka


	def onTechAcquired(self, iTech):
		pass


	def onSetPlayerAlive(self, argsList):
		'Set Player Alive Event'
		iPlayer, bNewValue = argsList
		
		iHuman = utils.getHumanID()
		if iPlayer == iHuman: 
			return
		
		# degrade Nubia when Makuria collapses to make the land less attractive to Mamluks
		if iPlayer == con.iMakuria and not bNewValue:
			map = CyMap()
			for i in range(map.numPlots()):
				plot = map.plotByIndex(i)
				if plot.getRegionID() in [con.rNobatia, con.rMakuria, con.rAlodia, con.rAksum]:
					if plot.getOwner() != iHuman:
						iImprovement = plot.getImprovementType()
						if iImprovement == con.iHamlet:
							plot.setImprovementType(con.iCottage)
						elif iImprovement == con.iVillage:
							plot.setImprovementType(con.iCottage)
						elif iImprovement == con.iTown:
							plot.setImprovementType(con.iHamlet)
						elif iImprovement in [con.iCottage, con.iFarm, con.iWatermill]:
							if gc.getGame().getSorenRandNum(3, 'Remove improvement?') == 0:
								plot.setImprovementType(-1)
						elif plot.isCity():
							city = plot.getPlotCity()
							if city.getPopulation() > 1:
								if city.getPopulation() < 10:
									city.changePopulation(-1)
								else:
									city.changePopulation(-2)

#setImprovementType(ImprovementType eNewValue)
#setPlotType(PlotType eNewValue, BOOL bRecalculate, BOOL bRebuildGraphics)
#setTerrainType(TerrainType eNewValue, BOOL bRecalculate, BOOL bRebuildGraphics)