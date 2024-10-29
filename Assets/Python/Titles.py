# The Sword of Islam - Honorific Titles

from CvPythonExtensions import *
import CvUtil
import PyHelpers
import Consts as con
from StoredData import sd
from RFCUtils import utils

# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer

class Titles:


	def setup(self):
		
		self.checkPlayerTitle(con.iRomanEmperor, con.iByzantium)
		self.checkPlayerTitle(con.iCaliph, con.iAbbasids)


	def checkPlayerTitle(self, iTitle, iPlayer):
		"""Checks if the player is eligible for the given title."""
		
		if iPlayer >= con.iNumPlayers:
			return
		
		# Skip if title is already taken, unless previous owner is a vassal of iPlayer
		for iLoopPlayer in range(con.iNumPlayers):
			if gc.getTeam(gc.getPlayer(iLoopPlayer).getTeam()).getProjectCount(iTitle):
				if not gc.getTeam(gc.getPlayer(iLoopPlayer).getTeam()).isVassal(iPlayer):
					return
		
		iStateReligion = gc.getPlayer(iPlayer).getStateReligion()
		
		if iTitle == con.iRomanEmperor:
			if gc.getMap().plot(con.tConstantinople[0],con.tConstantinople[1]).getOwner() == iPlayer:
				iNumCities = 0
				regionList = [con.rThrace, con.rAsia, con.rBithynia, con.rLycia, con.rPontus, con.rGalatia, con.rPaphlagonia, con.rCilicia, con.rCappadocia, con.rLesserArmenia, con.rTrebizond]
				apCityList = PyPlayer(iPlayer).getCityList()
				for pCity in apCityList:
					if pCity.GetCy().plot().getRegionID() in regionList:
						iNumCities += 1
				if iNumCities >= 4:
					gc.getTeam(gc.getPlayer(iPlayer).getTeam()).changeProjectCount(iTitle, 1)

		elif iTitle == con.iCaliph:
			pBaghdad = gc.getMap().plot(con.tBaghdad[0], con.tBaghdad[1]).getPlotCity()
			if not pBaghdad is None and not pBaghdad.isNone():
				if pBaghdad.getOwner() == iPlayer and (iStateReligion == con.iSunni or iStateReligion == con.iShia):
					gc.getTeam(gc.getPlayer(iPlayer).getTeam()).changeProjectCount(iTitle, 1)
					# Fatimid UHV3
					if iPlayer == con.iFatimids:
						if sd.getGoal(con.iFatimids, 2) == -1:
							sd.setGoal(con.iFatimids, 2, 1)
							
		elif iTitle == con.iShahanshah:
			bControl = True
			for iRegion in con.lTitleRegions[con.iShahanshah]:
				if not utils.checkRegionControl(iPlayer, iRegion):
					bControl = False
					break
			if bControl:
				gc.getTeam(gc.getPlayer(iPlayer).getTeam()).changeProjectCount(iTitle, 1)
				gc.getPlayer(iPlayer).changeFreeCityCommerce(CommerceTypes.COMMERCE_CULTURE, 1)
				# Khwarezm, Safavid and AkKoyunlu UHVs
				if iPlayer == con.iKhwarezm:
					if sd.getGoal(con.iKhwarezm, 1) == -1:
						sd.setGoal(con.iKhwarezm, 1, 1)
				elif iPlayer == con.iAkKoyunlu:
					if sd.getGoal(con.iAkKoyunlu, 2) == -1:
						sd.setGoal(con.iAkKoyunlu, 2, 1)
				elif iPlayer == con.iSafavids:
					if sd.getGoal(con.iSafavids, 0) == -1:
						sd.setGoal(con.iSafavids, 0, 1)
				elif iPlayer == con.iBuyids:
					if sd.getGoal(con.iBuyids, 0) == -1:
						sd.setGoal(con.iBuyids, 0, 1)

		elif iTitle == con.iRaja:
			if iStateReligion != con.iHinduism:
				return
			iNumRegions = 0
			for iRegion in con.lTitleRegions[con.iRaja]:
				if utils.checkRegionControl(iPlayer, iRegion):
					iNumRegions += 1
					if iNumRegions == 6:
						gc.getTeam(gc.getPlayer(iPlayer).getTeam()).changeProjectCount(iTitle, 1)
						break
					
		elif iTitle == con.iSharif:
			if utils.checkRegionControl(iPlayer, con.rHejaz):
				if iStateReligion == con.iSunni or iStateReligion == con.iShia:
					gc.getTeam(gc.getPlayer(iPlayer).getTeam()).changeProjectCount(iTitle, 1)

		elif iTitle == con.iProtector:
			if gc.getMap().plot(con.tJerusalem[0],con.tJerusalem[1]).getOwner() == iPlayer:
				if iStateReligion == con.iCatholicism or iStateReligion == con.iOrthodoxy:
					gc.getTeam(gc.getPlayer(iPlayer).getTeam()).changeProjectCount(iTitle, 1)


	def onCityAcquired(self, argsList):
		iPreviousOwner, iNewOwner, city, bConquest, bTrade = argsList
		
		# Sharif of Mecca - lost immediately if Mecca is lost
		if (city.getX(), city.getY()) == con.tMecca:
			pTeam = gc.getTeam(gc.getPlayer(iPreviousOwner).getTeam())
			if pTeam.getProjectCount(con.iSharif):
				pTeam.changeProjectCount(con.iSharif, -1)
				self.checkPlayerTitle(con.iSharif, iNewOwner)
				return

		# Protector of Jerusalem - lost immediately if Jerusalem is lost
		if (city.getX(), city.getY()) == con.tJerusalem:
			pTeam = gc.getTeam(gc.getPlayer(iPreviousOwner).getTeam())
			if pTeam.getProjectCount(con.iProtector):
				pTeam.changeProjectCount(con.iProtector, -1)
				self.checkPlayerTitle(con.iProtector, iNewOwner)
				return
				
		for iTitle in range(con.iNumTitles):
			if city.plot().getRegionID() in con.lTitleRegions[iTitle]:
				self.checkPlayerTitle(iTitle, iNewOwner)


	def onCityBuilt(self, city):
		
		if (city.getX(), city.getY()) == con.tBaghdad:
			self.checkPlayerTitle(con.iCaliph, city.getOwner())
		elif city.plot().getRegionID() in con.lTitleRegions[con.iShahanshah]:
			self.checkPlayerTitle(con.iShahanshah, city.getOwner())
		elif city.plot().getRegionID() in con.lTitleRegions[con.iRaja]:
			self.checkPlayerTitle(con.iRaja, city.getOwner())


	def onPlayerChangeStateReligion(self, argsList):
		iPlayer, iNewReligion, iOldReligion = argsList
		
		pPlayer = gc.getPlayer(iPlayer)
		pTeam = gc.getTeam(pPlayer.getTeam())
		iStateReligion = pPlayer.getStateReligion()
		
		for iTitle in range(con.iNumTitles):
			if pTeam.getProjectCount(iTitle):
				if (iTitle in [con.iCaliph, con.iSharif] and iStateReligion != con.iSunni and iStateReligion != con.iShia) \
				or (iTitle == con.iProtector and iStateReligion != con.iCatholicism and iStateReligion != con.iOrthodoxy) \
				or (iTitle == con.iRaja and iStateReligion != con.iHinduism):
					pTeam.changeProjectCount(iTitle, -1)
					for iPlayer in range(con.iNumPlayers):
						self.checkPlayerTitle(iTitle, iPlayer)
			else:
				if (iTitle in [con.iCaliph, con.iSharif] and iStateReligion in [con.iSunni, con.iShia]) \
				or (iTitle == con.iProtector and iStateReligion in [con.iCatholicism, con.iOrthodoxy]) \
				or (iTitle == con.iRaja and iStateReligion == con.iHinduism):
					self.checkPlayerTitle(iTitle, iPlayer)


	def onSetPlayerAlive(self, argsList):
		iPlayer, bNewValue = argsList
		
		# remove titles
		if bNewValue == False:
			for iTitle in range(con.iNumTitles):
				pTeam = gc.getTeam(gc.getPlayer(iPlayer).getTeam())
				if pTeam.getProjectCount(iTitle):
					pTeam.changeProjectCount(iTitle, -1)
					if iTitle == con.iShahanshah:
						gc.getPlayer(iPlayer).changeFreeCityCommerce(CommerceTypes.COMMERCE_CULTURE, -1)
					if iTitle == con.iCaliph:
						sd.setVal('iLastHolyWarTurn', sd.getVal('iLastHolyWarTurn') - 1) # cancels holy war call
					for iLoopPlayer in range(con.iNumPlayers):
						if iLoopPlayer != iPlayer:
							self.checkPlayerTitle(iTitle, iLoopPlayer)