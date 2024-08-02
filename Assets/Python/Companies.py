# The Sword of Islam - Companies

from CvPythonExtensions import *
import CvUtil
import PyHelpers
import Consts as con
from StoredData import sd
from RFCUtils import utils
from operator import itemgetter

# globals
gc = CyGlobalContext()
localText = CyTranslator()
PyPlayer = PyHelpers.PyPlayer

iNumPlayers = con.iNumPlayers
iNumTotalPlayers = con.iNumTotalPlayers
iNumCompanies = con.iNumCompanies
iSufi = con.iSufi
iKarimi = con.iKarimi
iNizari = con.iNizari
iHospitallers = con.iHospitallers
iTemplars = con.iTemplars
iVenetians = con.iVenetians
iGenoans = con.iGenoans
iPortuguese = con.iPortuguese
iSilk = con.iSilk
iPisans = con.iPisans
iTamils = con.iTamils
tCompaniesBirth = con.tCompaniesBirth
tCompaniesDeath = con.tCompaniesDeath
tCompaniesLimit = con.tCompaniesLimit
lCompanyRegions = con.lCompanyRegions
iCatholicism = con.iCatholicism
iOrthodoxy = con.iOrthodoxy
iSunni = con.iSunni
iShia = con.iShia
iPortugal = con.iPortugal

class Companies:


	def checkTurn(self, iGameTurn):
		
		# Check if it's not too early
		iCompany = iGameTurn % iNumCompanies
		if iGameTurn < getTurnForYear(tCompaniesBirth[iCompany]):
			return
		
		# Check if it's not too late
		if iGameTurn > getTurnForYear(tCompaniesDeath[iCompany]):
			iMaxCompanies = 0
			# Do not dissolve the Templars while Jerusalem is under Catholic control
			if iCompany == iTemplars:
				plot = gc.getMap().plot(con.tJerusalem[0], con.tJerusalem[1])
				if plot.isCity():
					if gc.getPlayer(plot.getPlotCity().getOwner()).getStateReligion() == iCatholicism:
						iMaxCompanies = tCompaniesLimit[iCompany]
		else:
			iMaxCompanies = tCompaniesLimit[iCompany]
		
		# loop through all cities, check the company value for each and add the good ones to a list of tuples (city, value)
		cityValueList = []
		for iPlayer in range(iNumPlayers):
			apCityList = PyPlayer(iPlayer).getCityList()
			for pCity in apCityList:
				city = pCity.GetCy()
				iValue = self.getCityValue(city, iCompany)
				if iValue > 0: 
					cityValueList.append((city, iValue * 10 + gc.getGame().getSorenRandNum(10, 'random bonus')))
				elif city.isHasCorporation(iCompany): # quick check to remove companies
					city.setHasCorporation(iCompany, False, True, True)
		
		# sort cities from highest to lowest value
		cityValueList.sort(key=itemgetter(1), reverse=True)
		
		# count the number of companies
		iCompanyCount = 0
		for iLoopPlayer in range(iNumPlayers):
			if utils.isActive(iLoopPlayer):
				iCompanyCount += gc.getPlayer(iLoopPlayer).countCorporations(iCompany)
		
		# debugText = 'ID: %d, ' %(iCompany)
		# spread the company
		for i in range(len(cityValueList)):
			city = cityValueList[i][0]
			if city.isHasCorporation(iCompany):
				# debugText += '%s:%d(skip), ' %(city.getName(), cityValueList[i][1])
				continue
			if iCompanyCount >= iMaxCompanies and i >= iMaxCompanies: # don't spread to weak cities if the limit was reached
				# debugText += 'limit reached'
				break
			city.setHasCorporation(iCompany, True, True, True)
			# debugText += '%s(OK!), ' %(city.getName())
			break
		# utils.echo(debugText)
		
		# if the limit was exceeded, remove company from the worst city
		if iCompanyCount > iMaxCompanies:
			for i in range(len(cityValueList)-1, 0, -1):
				city = cityValueList[i][0]
				if city.isHasCorporation(iCompany):
					city.setHasCorporation(iCompany, False, True, True)
					break


	def onPlayerChangeStateReligion(self, argsList):
		iPlayer, iNewReligion, iOldReligion = argsList
		
		apCityList = PyPlayer(iPlayer).getCityList()
		for pCity in apCityList:
			city = pCity.GetCy()
			for iCompany in range(iNumCompanies):
				if city.isHasCorporation(iCompany):
					if self.getCityValue(city, iCompany) < 0:
						city.setHasCorporation(iCompany, False, True, True)


	def onCityAcquired(self, argsList):
		iPreviousOwner, iNewOwner, city, bConquest, bTrade = argsList
		
		for iCompany in range(iNumCompanies):
			if city.isHasCorporation(iCompany):
				if self.getCityValue(city, iCompany) < 0:
					city.setHasCorporation(iCompany, False, True, True)


	def getCityValue(self, city, iCompany):
		
		if city is None: return -1
		elif city.isNone(): return -1
		
		iValue = 0
		
		owner = gc.getPlayer(city.getOwner())
		ownerTeam = gc.getTeam(owner.getTeam())
		
		# Mevlevi Order
		if iCompany == iSufi and city.getNumRealBuilding(con.iMevlanasTomb) > 0:
			return 100
		
		# Safavid Sufi Order
		if iCompany == iSufi and city.getOwner() == con.iSafavids and (city.getX(), city.getY()) == con.tArdabil:
			return 100

		# Tamils more likely to expand into Gujarati cities
		if iCompany == iTamils and city.getOwner() == con.iGujarat:
			iValue += 3
		
		# Stop Damascus' culture from attacking Northern Syria
		if iCompany == iSufi and (city.getX(), city.getY()) == con.tDamascus and utils.getYear() < 1000:
			iValue -= 2
		
		# spread the Portuguese to Portuguese cities and don't spread if at war with Portugal
		if iCompany == iPortuguese:
			if owner.getID() == iPortugal:
				return 100
			elif ownerTeam.isAtWar(iPortugal):
				return -1
		
		# no Italians if Latins were massacred recently
		if city.getOwner() == con.iByzantium and sd.getVal('iLatinMassacreTurn'):
			if gc.getGame().getGameTurn() < sd.getVal('iLatinMassacreTurn') + utils.getTurns(25):
				return -1
		
		# don't spread European companies if at war with Crusaders
		if iCompany in [iVenetians, iGenoans, iPisans, iPortuguese]:
			if owner.getStateReligion() != iCatholicism and owner.getStateReligion() != iOrthodoxy:
				if (ownerTeam.isAtWar(con.iCrusaders) and gc.getPlayer(con.iCrusaders).isAlive()) \
				or (ownerTeam.isAtWar(con.iAntioch) and gc.getPlayer(con.iAntioch).isAlive()):
					return -1
		
		# state religion requirements
		iStateReligion = owner.getStateReligion()
		if iCompany == iHospitallers or iCompany == iTemplars:
			if iStateReligion == iCatholicism:
				iValue += 3
			elif iStateReligion == iOrthodoxy:
				iValue += 1
			else:
				return -1
		elif iCompany == iKarimi:
			if iStateReligion != iSunni and iStateReligion != iShia:
				return -1
		elif iCompany == iSufi:
			if iStateReligion != iSunni and iStateReligion != iShia:
				return -1
		
		# state monopoly
		if iCompany not in [iSufi, iNizari] and owner.getCivics(3) == con.iStateMonopolyCivic: 
			return -1
		
		# geographical requirements
		plot = gc.getMap().plot(city.getX(),city.getY())
		if len(lCompanyRegions[iCompany]) > 0 and plot.getRegionID() not in lCompanyRegions[iCompany]:
			return -1
		if iCompany == iHospitallers and iStateReligion == iCatholicism:
			if plot.getRegionID() == con.rNorthernSyria: # preference for Antioch
				iValue += 1
			elif plot.getRegionID() == con.rRhodes: # Knights of Rhodes
				if city.getOwner() == con.iCrusaders and sd.getCivStatus(city.getOwner()) == 1:
					iValue += 3
				else:
					iValue += 1
		elif iCompany == iKarimi:
			if plot.getRegionID() in [con.rLowerEgypt, con.rHejaz, con.rYemen]:
				iValue += 1
		
		# trade companies - coastal cities only
		if iCompany == iVenetians or iCompany == iGenoans or iCompany == iPisans or iCompany == iPortuguese:
			if not city.isCoastal(20):
				return -1
		elif iCompany == iKarimi:
			if not city.isCoastal(20):
				iValue -= 1
		
		# bonus for religions
		if iCompany == iNizari:
			if not city.isHasReligion(iShia):
				return -1
			if iStateReligion == iShia:
				iValue += 1
		elif iCompany == iSufi:
			if not city.isHasReligion(iSunni) and not city.isHasReligion(iShia):
				return -1
		elif iCompany == iKarimi:
			if not city.isHasReligion(iSunni) and not city.isHasReligion(iShia):
				return -1
			if iStateReligion == iCatholicism or iStateReligion == iOrthodoxy:
				iValue -= 1
		else:
			if iStateReligion == iCatholicism:
				iValue += 3
			elif iStateReligion == iOrthodoxy:
				iValue += 1
			elif iStateReligion == iSunni or iStateReligion == iShia:
				iValue -= 1
			if city.isHasReligion(iCatholicism):
				iValue += 2
			elif city.isHasReligion(iOrthodoxy):
				iValue += 1
		
		# various bonuses
		if iCompany == iHospitallers or iCompany == iTemplars:
			if city.getNumRealBuilding(con.iWalls) > 0: iValue += 1
			if city.getNumRealBuilding(con.iCastle) > 0 or city.getNumRealBuilding(con.iQalat) > 0: iValue += 1
			if city.getNumRealBuilding(con.iBarracks) > 0: iValue += 1
			if city.getNumRealBuilding(con.iStable) > 0: iValue += 1
			if city.getNumRealBuilding(con.iArcheryRange) > 0 or city.getNumRealBuilding(con.iBowyer) > 0: iValue += 1
			if iCompany == iHospitallers and city.getNumRealBuilding(con.iKrakDesChevaliers) > 0: iValue += 5
			if iCompany == iTemplars and city.getNumRealBuilding(con.iDomeOfTheRock) > 0: iValue += 5
		
		elif iCompany == iSufi:
			if city.getNumRealBuilding(con.iLibrary) > 0: iValue += 1
			if city.getNumRealBuilding(con.iUniversity) > 0 or city.getNumRealBuilding(con.iNizamiyya) > 0: iValue += 1
			if city.getNumRealBuilding(con.iSunniTemple) > 0: iValue += 1
			elif city.getNumRealBuilding(con.iShiaTemple) > 0: iValue += 1
			if city.getNumRealBuilding(con.iSunniCathedral) > 0: iValue += 1
			elif city.getNumRealBuilding(con.iShiaCathedral) > 0: iValue += 1
			if city.getNumRealBuilding(con.iSunniMonastery) > 0: iValue += 1
			elif city.getNumRealBuilding(con.iShiaMonastery) > 0: iValue += 1
			if city.getNumRealBuilding(con.iHan) > 0: iValue += 1
			if city.getNumRealBuilding(con.iBrothel) > 0: iValue -= 1
			if city.getNumRealBuilding(con.iSufiShrine) > 0: iValue += 1
			if owner.getCivics(3) == con.iPersecutionCivic: iValue -= 2
			iValue += (utils.getFavorLevel(city.getOwner()) - 4) / 2
			# bonus from Mevlana's Tomb
			if sd.getVal('iMevlanaOwner') == city.getOwner(): iValue += 1
		
		elif iCompany == iNizari:
			if city.getNumRealBuilding(con.iWalls) > 0: iValue += 1
			if city.getNumRealBuilding(con.iCastle) > 0: iValue += 1
			if city.getNumRealBuilding(con.iInn) > 0 or city.getNumRealBuilding(con.iCaravanserai) > 0 or city.getNumRealBuilding(con.iHan) > 0: iValue += 2
			if city.getNumRealBuilding(con.iBrothel) > 0: iValue += 2
			if city.getNumRealBuilding(con.iDenOfSpies) > 0: iValue += 2
			if owner.getCivics(3) == con.iPersecutionCivic: iValue -= 2
		
		else:
			iValue += city.getTradeRoutes() - 1
			if city.getNumRealBuilding(con.iHarbor) > 0: iValue += 1
			if city.getNumRealBuilding(con.iMarket) > 0: iValue += 1
			if city.getNumRealBuilding(con.iBank) > 0: iValue += 1
			if city.getNumRealBuilding(con.iTextileMill) > 0: iValue += 1
			if city.getNumRealBuilding(con.iSlaveMarket) > 0: iValue += 1
			if owner.getCivics(3) == con.iMarketEconomyCivic: iValue += 1
			elif owner.getCivics(3) == con.iMerchantCapitalismCivic: iValue += 2
			if iCompany == iKarimi:
				if city.getNumRealBuilding(con.iInn) > 0 or city.getNumRealBuilding(con.iCaravanserai) > 0 or city.getNumRealBuilding(con.iHan) > 0: iValue += 1
				if city.getNumRealBuilding(con.iGreatLighthouse) > 0: iValue += 2
		
		# resources
		iTempValue = 0
		bFound = False
		for i in range(4):
			iBonus = gc.getCorporationInfo(iCompany).getPrereqBonus(i)
			if iBonus > -1:
				if city.getNumBonuses(iBonus) > 0: bFound = True
				if iCompany in [iKarimi, iHospitallers, iTemplars, iNizari]:
					iTempValue += city.getNumBonuses(iBonus)
				else:
					iTempValue += city.getNumBonuses(iBonus) * 2
		if iCompany in [iKarimi, iVenetians, iGenoans] and not bFound: return -1
		iValue += iTempValue
		
		# competition
		if iCompany == iHospitallers and city.isHasCorporation(iTemplars): iValue *= 0.66
		elif iCompany == iTemplars and city.isHasCorporation(iHospitallers): iValue *= 0.66
		elif iCompany == iKarimi and (city.isHasCorporation(iVenetians) or city.isHasCorporation(iGenoans) or city.isHasCorporation(iPisans)): iValue /= 2
		elif iCompany == iVenetians and (city.isHasCorporation(iGenoans) or city.isHasCorporation(iKarimi) or city.isHasCorporation(iPisans)): iValue /= 2
		elif iCompany == iGenoans and (city.isHasCorporation(iVenetians) or city.isHasCorporation(iKarimi) or city.isHasCorporation(iPisans)): iValue /= 2
		elif iCompany == iPisans and (city.isHasCorporation(iVenetians) or city.isHasCorporation(iKarimi) or city.isHasCorporation(iGenoans)): iValue /= 2
		
		# threshold
		if iValue < 3: return -1
		
		# spread it out
		iValue -= owner.countCorporations(iCompany)
		
		return iValue