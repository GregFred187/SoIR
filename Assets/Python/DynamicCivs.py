# Dynamic Civs - edead

from CvPythonExtensions import *
import CvUtil
import PyHelpers
import Consts as con
from StoredData import sd
from RFCUtils import utils

# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer
PyInfo = PyHelpers.PyInfo
localText = CyTranslator()
iNumPlayers = con.iNumPlayers


class DynamicCivs:


	def __init__(self):
		
		self.defaultNames = {
			con.iByzantium : "TXT_KEY_CIV_BYZANTIUM_DESC_DEFAULT",
			con.iMakuria : "TXT_KEY_CIV_MAKURIA_DESC_DEFAULT",
			con.iAbbasids : "TXT_KEY_CIV_ABBASIDS_DESC_DEFAULT",
			con.iKhazars : "TXT_KEY_CIV_KHAZARS_DESC_DEFAULT",
			con.iChauhan : "TXT_KEY_CIV_CHAUHAN_DESC_DEFAULT",
			con.iMalwa : "TXT_KEY_CIV_MALWA_DESC_DEFAULT",
			con.iOghuz : "TXT_KEY_CIV_OGHUZ_DESC_DEFAULT",
			con.iSamanids: "TXT_KEY_CIV_SAMANIDS_DESC_DEFAULT",
			con.iKhanids: "TXT_KEY_CIV_KHANIDS_DESC_DEFAULT",
			con.iArmenia : "TXT_KEY_CIV_ARMENIA_DESC_DEFAULT",
			con.iKiev : "TXT_KEY_CIV_KIEV_DESC_DEFAULT",
			con.iAlans : "TXT_KEY_CIV_ALANS_DESC_DEFAULT",
			con.iYemen: "TXT_KEY_CIV_YEMEN_DESC_DEFAULT",
			con.iBuyids : "TXT_KEY_CIV_BUYIDS_DESC_DEFAULT",
			con.iGujarat : "TXT_KEY_CIV_GUJARAT_DESC_DEFAULT",
			con.iGhaznavids : "TXT_KEY_CIV_GHAZNAVIDS_DESC_DEFAULT",
			con.iFatimids : "TXT_KEY_CIV_FATIMIDS_DESC_DEFAULT",
			con.iChalukya : "TXT_KEY_CIV_CHALUKYA_DESC_DEFAULT",
			con.iGeorgia : "TXT_KEY_CIV_GEORGIA_DESC_DEFAULT",
			con.iSeljuks : "TXT_KEY_CIV_SELJUKS_DESC_DEFAULT",
			con.iKypchaks : "TXT_KEY_CIV_KYPCHAKS_DESC_DEFAULT",
			con.iSindh : "TXT_KEY_CIV_SINDH_DESC_DEFAULT",
			con.iRum : "TXT_KEY_CIV_TURKS_DESC_DEFAULT",
			con.iKhwarezm: "TXT_KEY_CIV_KHWAREZM_DESC_DEFAULT",
			con.iAntioch: "TXT_KEY_CIV_ANTIOCH_DESC_DEFAULT",
			con.iCrusaders: "TXT_KEY_CIV_OUTREMER_DESC_DEFAULT",
			con.iZengids: "TXT_KEY_CIV_ZENGIDS_DESC_DEFAULT",
			con.iKhitai: "TXT_KEY_CIV_KHITAI_DESC_DEFAULT",
			con.iGhorids: "TXT_KEY_CIV_GHORIDS_DESC_DEFAULT",
			con.iOman: "TXT_KEY_CIV_OMAN_DESC_DEFAULT",
			con.iAyyubids: "TXT_KEY_CIV_AYYUBIDS_DESC_DEFAULT",
			con.iMongols: "TXT_KEY_CIV_MONGOLS_DESC_DEFAULT",
			con.iGolden: "TXT_KEY_CIV_GOLDEN_DESC_DEFAULT",
			con.iMamluks: "TXT_KEY_CIV_MAMLUKS_DESC_DEFAULT",
			con.iChagatai: "TXT_KEY_CIV_CHAGATAI_DESC_DEFAULT",
			con.iOttomans : "TXT_KEY_CIV_OTTOMAN_DESC_DEFAULT",
			con.iBahmanids : "TXT_KEY_CIV_BAHMANIDS_DESC_DEFAULT",
			con.iTimurids: "TXT_KEY_CIV_TIMURIDS_DESC_DEFAULT",
			con.iAkKoyunlu: "TXT_KEY_CIV_AKKOYUNLU_DESC_DEFAULT",
			con.iSafavids: "TXT_KEY_CIV_SAFAVIDS_DESC_DEFAULT",
			con.iPortugal: "TXT_KEY_CIV_PORTUGAL_DESC_DEFAULT",
			con.iMughals: "TXT_KEY_CIV_MUGHALS_DESC_DEFAULT",
		}
		
		self.vassalNames = {
			con.iByzantium : "TXT_KEY_CIV_BYZANTIUM_DESC_VASSAL",
			con.iMakuria : "TXT_KEY_CIV_MAKURIA_DESC_VASSAL",
			con.iAbbasids : "TXT_KEY_CIV_ABBASIDS_DESC_VASSAL",
			con.iKhazars : "TXT_KEY_CIV_KHAZARS_DESC_VASSAL",
			con.iChauhan : "TXT_KEY_CIV_CHAUHAN_DESC_VASSAL",
			con.iMalwa : "TXT_KEY_CIV_MALWA_DESC_VASSAL",
			con.iOghuz : "TXT_KEY_CIV_OGHUZ_DESC_DEFAULT",
			con.iSamanids : "TXT_KEY_CIV_SAMANIDS_DESC_VASSAL",
			con.iKhanids: "TXT_KEY_CIV_KHANIDS_DESC_DEFAULT",		   
			con.iArmenia : "TXT_KEY_CIV_ARMENIA_DESC_VASSAL",
			con.iKiev : "TXT_KEY_CIV_KIEV_DESC_VASSAL",
			con.iAlans : "TXT_KEY_CIV_ALANS_DESC_VASSAL",	   
			con.iYemen: "TXT_KEY_CIV_YEMEN_DESC_VASSAL",
			con.iBuyids : "TXT_KEY_CIV_BUYIDS_DESC_VASSAL",
			con.iGujarat : "TXT_KEY_CIV_GUJARAT_DESC_VASSAL",
			con.iGhaznavids : "TXT_KEY_CIV_GHAZNAVIDS_DESC_VASSAL",
			con.iFatimids : "TXT_KEY_CIV_FATIMIDS_DESC_VASSAL",
			con.iGeorgia : "TXT_KEY_CIV_GEORGIA_DESC_VASSAL",
			con.iSeljuks : "TXT_KEY_CIV_SELJUKS_DESC_VASSAL",
			con.iSindh : "TXT_KEY_CIV_SINDH_DESC_VASSAL",
			con.iRum : "TXT_KEY_CIV_TURKS_DESC_VASSAL",
			con.iKhwarezm: "TXT_KEY_CIV_KHWAREZM_DESC_VASSAL",
			con.iAntioch: "TXT_KEY_CIV_ANTIOCH_DESC_VASSAL",
			con.iCrusaders: "TXT_KEY_CIV_OUTREMER_DESC_VASSAL",
			con.iZengids: "TXT_KEY_CIV_ZENGIDS_DESC_VASSAL",
			con.iKhitai: "TXT_KEY_CIV_KHITAI_DESC_DEFAULT",		 
			con.iGhorids: "TXT_KEY_CIV_GHORIDS_DESC_VASSAL",
			con.iAyyubids: "TXT_KEY_CIV_AYYUBIDS_DESC_VASSAL",
			con.iMongols: "TXT_KEY_CIV_MONGOLS_DESC_VASSAL",			
			con.iMamluks: "TXT_KEY_CIV_MAMLUKS_DESC_VASSAL",
			con.iChagatai: "TXT_KEY_CIV_CHAGATAI_DESC_DEFAULT",
			con.iGolden: "TXT_KEY_CIV_GOLDEN_DESC_DEFAULT",
			con.iKypchaks : "TXT_KEY_CIV_KYPCHAKS_DESC_DEFAULT",
			con.iChalukya : "TXT_KEY_CIV_CHALUKYA_DESC_DEFAULT",
			con.iOttomans : "TXT_KEY_CIV_OTTOMAN_DESC_VASSAL",
			con.iBahmanids : "TXT_KEY_CIV_BAHMANIDS_DESC_VASSAL",
			con.iTimurids: "TXT_KEY_CIV_TIMURIDS_DESC_VASSAL",
			con.iAkKoyunlu: "TXT_KEY_CIV_AKKOYUNLU_DESC_VASSAL",
			con.iSafavids: "TXT_KEY_CIV_SAFAVIDS_DESC_VASSAL",
			con.iPortugal: "TXT_KEY_CIV_PORTUGAL_DESC_VASSAL",
			con.iMughals: "TXT_KEY_CIV_MUGHALS_DESC_VASSAL",
		}
		
		self.respawnedNames = {
			con.iArmenia : "TXT_KEY_CIV_CILICIA_DESC_DEFAULT",
			con.iCrusaders : "TXT_KEY_CIV_CYPRUS_DESC_DEFAULT",
			con.iGhorids : "TXT_KEY_CIV_DELHI_DESC_DEFAULT",
			con.iKiev : "TXT_KEY_CIV_KIEV_DESC_RESPAWN",
			con.iChauhan : "TXT_KEY_CIV_MEWAR_DESC_DEFAULT",
			con.iChalukya : "TXT_KEY_CIV_SEUNA_DESC_DEFAULT",
			con.iRum : "TXT_KEY_CIV_KARAMAN_DESC_DEFAULT",
			con.iMongols: "TXT_KEY_CIV_JALAYIRDS_DESC_DEFAULT",
			con.iKhwarezm : "TXT_KEY_CIV_BUKHARA_DESC_DEFAULT",
			con.iGhaznavids : "TXT_KEY_CIV_KARTIDS_DESC_DEFAULT",
			con.iBuyids : "TXT_KEY_CIV_MUZZ_DESC_DEFAULT",
			con.iSeljuks : "TXT_KEY_CIV_KARA_DESC_DEFAULT",
			con.iChagatai : "TXT_KEY_CIV_MOG_DESC_DEFAULT",
			con.iBahmanids : "TXT_KEY_CIV_BIJ_DESC",
			con.iGolden : "TXT_KEY_CIV_CRIMEAN_DESC_DEFAULT",
			con.iKhanids: "TXT_KEY_CIV_KAZAK_DESC_DEFAULT",
			con.iKhazars: "TXT_KEY_CIV_KALMYK_DESC_DEFAULT",
			con.iAlans: "TXT_KEY_CIV_CIRCASSIA_DESC_DEFAULT",
			con.iKypchaks: "TXT_KEY_CIV_NOGAI_DESC_DEFAULT",
			con.iKhitai: "TXT_KEY_CIV_ZUNGHAR_DESC_DEFAULT",		
		}
		
		self.sunniNames = {
			con.iGujarat : "TXT_KEY_CIV_GUJARAT_SULTANATE_DESC_DEFAULT",
			con.iMalwa : "TXT_KEY_CIV_MALWA_SULTANATE_DESC_DEFAULT",
			con.iSindh : "TXT_KEY_CIV_SINDH_SULTANATE_DESC_DEFAULT",
			con.iYemen : "TXT_KEY_CIV_YEMEN_SULTANATE_DESC_DEFAULT",
		}
		
		self.shiaNames = {
			con.iGujarat : "TXT_KEY_CIV_GUJARAT_SULTANATE_DESC_DEFAULT",
			con.iMalwa : "TXT_KEY_CIV_MALWA_SULTANATE_DESC_DEFAULT",
			con.iOman : "TXT_KEY_CIV_OMAN_IMAMATE_DESC",
			con.iAyyubids: "TXT_KEY_CIV_AYYUBID_KINGDOM_DESC",
		}
		
		self.nonIslamicNames = {
			con.iAbbasids : "TXT_KEY_CIV_MESOPOTAMIA_DESC",
			con.iFatimids : "TXT_KEY_CIV_FATIMID_KINGDOM_DESC",
			con.iYemen : "TXT_KEY_CIV_YEMEN_KINGDOM_DESC_DEFAULT",
			con.iZengids : "TXT_KEY_CIV_MOSUL_KINGDOM_DESC_DEFAULT",
			con.iGhaznavids : "TXT_KEY_CIV_GHAZNAVID_KINGDOM_DESC_DEFAULT",
			con.iRum : "TXT_KEY_CIV_TURKS_KINGDOM_DESC_DEFAULT",
			con.iOttomans : "TXT_KEY_CIV_OTTOMAN_KINGDOM_DESC_DEFAULT",
			con.iBahmanids : "TXT_KEY_CIV_BAHMANID_KINGDOM_DESC_DEFAULT",
			con.iAyyubids: "TXT_KEY_CIV_AYYUBID_KINGDOM_DESC",
		}
		
		self.empireNames = {
			con.iMakuria : "TXT_KEY_CIV_NUBIAN_EMPIRE_DESC",
			con.iArmenia : "TXT_KEY_CIV_ARMENIAN_EMPIRE_DESC",
			con.iGeorgia : "TXT_KEY_CIV_GEORGIAN_EMPIRE_DESC",
			con.iChauhan : "TXT_KEY_CIV_CHAUHAN_EMPIRE_DESC",
			con.iGujarat : "TXT_KEY_CIV_SOLANKI_EMPIRE_DESC",
			con.iMalwa : "TXT_KEY_CIV_PARAMARA_EMPIRE_DESC",
			con.iKhanids: "TXT_KEY_CIV_KHANIDS_EMPIRE_DESC",
			con.iChalukya : "TXT_KEY_CIV_CHALUKYAEMP_DESC_DEFAULT",		 
			con.iBahmanids : "TXT_KEY_CIV_BAHMANID_EMPIRE_DESC",
			con.iCrusaders : "TXT_KEY_CIV_LATIN_EMPIRE_DESC",
			con.iGhorids : "TXT_KEY_CIV_GHORID_EMPIRE_DESC",
			con.iGhaznavids : "TXT_KEY_CIV_GHAZNAVID_EMPIRE_DESC",
			con.iSamanids : "TXT_KEY_CIV_SAMANID_EMPIRE_DESC",
			con.iKhwarezm : "TXT_KEY_CIV_KHWAREZM_EMPIRE_DESC",
			con.iOttomans : "TXT_KEY_CIV_OTTOMAN_DESC_DEFAULT",
			con.iBuyids : "TXT_KEY_CIV_BUYID_EMPIRE_DESC",
		}
		
		self.specialNames = {
			con.iBahmanids : "TXT_KEY_CIV_BIJ_DESC",
			con.iMongols : "TXT_KEY_CIV_MONGILK_DESC",  
		}	   
		

	def setCivDesc(self, iCiv, sName, sShort="", sAdj=""):
	
		gc.getPlayer(iCiv).setCivName(localText.getText(sName, ()), localText.getText(sShort, ()), localText.getText(sAdj, ()))


	def setup(self):
		
		for iPlayer in range(con.iNumPlayers):
			self.setCivDesc(iPlayer, self.defaultNames[iPlayer])


	def checkName(self, iPlayer):
	
		if iPlayer >= iNumPlayers: return
	
		bVassal = utils.isAVassal(iPlayer)
		pPlayer = gc.getPlayer(iPlayer)
		bRespawned = sd.getCivStatus(iPlayer)
		iReligion = pPlayer.getStateReligion()
		capital = gc.getPlayer(iPlayer).getCapitalCity()
		
		# respawn > capital > religion > empire > vassal
		
		# special case: Islamic Armenia
		if iPlayer == con.iArmenia and (pPlayer.getNumCities() == 0 or capital.plot().getRegionID() not in [con.rCilicia, con.rVaspurakan]):
			bForced = False
			if bVassal:
				iMasterReligion = gc.getPlayer(utils.getMaster(iPlayer)).getStateReligion()
				if iMasterReligion in [con.iSunni, con.iShia]:
					bForced = True
			if iReligion in [con.iSunni, con.iShia] or bForced:
				self.setCivDesc(iPlayer, "TXT_KEY_CIV_ARMENISTAN_DESC", "TXT_KEY_CIV_ARMENISTAN_DESC")
				return
		
		if iPlayer == con.iMongols and gc.getPlayer(con.iChagatai).isAlive():
			if iPlayer == utils.getHumanID():
				self.setCivDesc(iPlayer, "TXT_KEY_CIV_MONGILK_DESC", "TXT_KEY_CIV_MONGILK_DESC")
			elif iPlayer != utils.getHumanID() and gc.getGame().getGameTurnYear() < 1336:
				self.setCivDesc(iPlayer, "TXT_KEY_CIV_MONGILK_DESC", "TXT_KEY_CIV_MONGILK_DESC")
			return
			
		if iPlayer == con.iKiev and gc.getGame().getGameTurnYear() > 1470:
			if iPlayer != utils.getHumanID():
				self.setCivDesc(iPlayer, "TXT_KEY_CIV_VOI_DESC", "TXT_KEY_CIV_KIEV_SHORT_DESC")
			return
			
		if iPlayer == con.iMakuria and gc.getGame().getGameTurnYear() > 1180 and utils.checkRegionOwnedCity(con.iMakuria, con.rAlodia) and pPlayer.getNumCities() < 12:
			if not bVassal:
				self.setCivDesc(iPlayer, "TXT_KEY_CIV_DOTAWO_DESC", "TXT_KEY_CIV_DOTAWO_DESC")
			return
			
		#if iPlayer == con.iBahmanids and gc.getGame().getGameTurnYear() > 1488 and not utils.checkRegionOwnedCity(iBahmanids, con.rTelangana) and not utils.checkRegionOwnedCity(iBahmanids, con.rMalwa):
			#self.setCivDesc(iPlayer, "TXT_KEY_CIV_BIJ_DESC", "TXT_KEY_CIV_BIJ_DESC")
			#return

		# by respawns
		if bRespawned and iPlayer in self.respawnedNames and iPlayer != con.iArmenia:
			if iPlayer == con.iKhwarezm:
				if pPlayer.getNumCities() >= 8 and not bVassal:
					self.setCivDesc(iPlayer, "TXT_KEY_CIV_SHAYBANIDS_DESC_DEFAULT")
				elif capital.plot().getRegionID() == con.rKhwarezm:
					self.setCivDesc(iPlayer, "TXT_KEY_CIV_KHIVA_DESC_DEFAULT")
				elif capital.plot().getRegionID() == con.rFarghana:
					self.setCivDesc(iPlayer, "TXT_KEY_CIV_KOKAND_DESC_DEFAULT")
				elif capital.plot().getRegionID() == con.rSogd:
					self.setCivDesc(iPlayer, "TXT_KEY_CIV_BUKHARA_DESC_DEFAULT")
			elif iPlayer == con.iChalukya:
				if pPlayer.getNumCities() >= 8 and not bVassal:
					self.setCivDesc(iPlayer, "TXT_KEY_CIV_SEUNAEMPIRE_DESC_DEFAULT")
			elif iPlayer == con.iAlans:
				if bVassal:
					self.setCivDesc(iPlayer, "TXT_KEY_CIV_CIRCASSIA_DESC_VASSAL")
				else:
					self.setCivDesc(iPlayer, "TXT_KEY_CIV_CIRCASSIA_DESC_DEFAULT")
			elif iPlayer == con.iGhorids:
				if iReligion not in [con.iSunni, con.iShia]:
					self.setCivDesc(iPlayer, "TXT_KEY_CIV_DELHI_KINGDOM_DESC_DEFAULT")
				else:
					plot = gc.getMap().plot(con.tDelhi[0], con.tDelhi[1])
					if plot.isCity():
						city = plot.getPlotCity()
						if city.getOwner() == iPlayer:
							self.setCivDesc(iPlayer, self.respawnedNames[iPlayer], "TXT_KEY_CIV_DELHI_SHORT_DESC", "TXT_KEY_CIV_DELHI_ADJECTIVE")
			elif iPlayer == con.iRum:
				if pPlayer.getNumCities() >= 8 and not bVassal:
					self.setCivDesc(iPlayer, "TXT_KEY_CIV_KARAMANID_EMPIRE_DESC")
			return
		
		# by vassalage
		if bVassal and iPlayer in self.vassalNames:
			#if iPlayer == con.iBahmanids and gc.getGame().getGameTurnYear() > 1488 and not utils.checkRegionOwnedCity(iBahmanids, con.rTelangana) and not utils.checkRegionOwnedCity(iBahmanids, con.rMalwa):
				#szName = self.specialNames[iPlayer]
			#else:
			szName = self.vassalNames[iPlayer]
		else:
			szName = self.defaultNames[iPlayer]

		# by status (empires)
		if not bVassal:
			iCivic = pPlayer.getCivics(0)
			if iPlayer in self.empireNames:
				minCities = 8 # 8/6
				if iPlayer in [con.iSamanids, con.iBuyids]: minCities = 4 # 4/3
				elif iPlayer in [con.iArmenia, con.iGeorgia, con.iCrusaders, con.iMakuria]: minCities = 16 # 16/12
				if iCivic == con.iEmpireCivic or iCivic == con.iAbsolutismCivic or pPlayer.getNumCities() >= minCities:
					if pPlayer.getNumCities() >= (minCities * 3 / 4):
						szName = self.empireNames[iPlayer]

		# by religion
		if iPlayer in self.sunniNames and iReligion == con.iSunni:
			szName = self.sunniNames[iPlayer]
			if iPlayer == con.iGujarat and iPlayer != utils.getHumanID():
				pPlayer.setName(localText.getText("TXT_KEY_LEADER_AHMAD_SHAH", ()))
			if iPlayer == con.iMalwa and iPlayer != utils.getHumanID():
				pPlayer.setName(localText.getText("TXT_KEY_LEADER_HOSHANG_SHAH", ()))
		if iPlayer in self.shiaNames and iReligion == con.iShia:
			szName = self.shiaNames[iPlayer]
		if iPlayer in self.nonIslamicNames and iReligion not in [con.iSunni, con.iShia]:
			szName = self.nonIslamicNames[iPlayer]
		
		# by capitals
		if capital and capital.plot():
			if iPlayer == con.iAntioch:
				if capital.plot().getRegionID() == con.rNorthernSyria and capital.getName() == "Tripoli":
					self.setCivDesc(iPlayer, "TXT_KEY_CIV_TRIPOLI_DESC", "TXT_KEY_CIV_TRIPOLI_SHORT_DESC")
					return
				elif capital.plot().getRegionID() == con.rEdessa:
					self.setCivDesc(iPlayer, "TXT_KEY_CIV_EDESSA_DESC", "TXT_KEY_CIV_EDESSA_SHORT_DESC")
					return
			elif iPlayer == con.iCrusaders:
				if capital.plot().getRegionID() == con.rPalestine and capital.getName() == "Acre":
					self.setCivDesc(iPlayer, "TXT_KEY_CIV_ACRE_DESC", "TXT_KEY_CIV_ACRE_SHORT_DESC")
					return
			elif iPlayer == con.iAyyubids:
				if pPlayer.getNumCities() < 6 or bVassal:
					if capital.plot().getRegionID() == con.rSyria and capital.getName() == "Dimashq":
						self.setCivDesc(iPlayer, "TXT_KEY_CIV_DAMASCUS_DESC")
						return
					elif capital.plot().getRegionID() == con.rSyria and capital.getName() == "Homs":
						self.setCivDesc(iPlayer, "TXT_KEY_CIV_HOMS_DESC")
						return
			elif iPlayer == con.iSeljuks:
				if pPlayer.getNumCities() < 6 or bVassal:
					if capital.plot().getRegionID() == con.rKerman and capital.getName() == "Kerman":
						self.setCivDesc(iPlayer, "TXT_KEY_CIV_KERMAN_DESC")
						return
					elif capital.plot().getRegionID() == con.rLuristan and capital.getName() == "Hamadan":
						self.setCivDesc(iPlayer, "TXT_KEY_CIV_HAMADAN_DESC")
						return
			elif iPlayer == con.iArmenia:
				if capital.plot().getRegionID() == con.rVaspurakan:
					self.setCivDesc(iPlayer, "TXT_KEY_CIV_VASPURAKAN_DESC_DEFAULT")
					return
				elif capital.plot().getRegionID() == con.rCilicia:
					self.setCivDesc(iPlayer, "TXT_KEY_CIV_CILICIA_DESC_DEFAULT")
					return
				elif bRespawned and capital.plot().getRegionID() in [con.rGreaterArmenia, con.rKars]:
					if bVassal:
						self.setCivDesc(iPlayer, "TXT_KEY_CIV_ARMENIA_DESC_VASSAL")
						return
					else:
						self.setCivDesc(iPlayer, "TXT_KEY_CIV_ARMENIA_DESC_DEFAULT")
						return
		
		self.setCivDesc(iPlayer, szName)


	def onCivRespawn(self, iPlayer):
		
		pPlayer = gc.getPlayer(iPlayer)
		
		# change balance modifiers for respawned civs - use modifiers of a civ that spawns around the same time for convenience
		if sd.getCivStatus(iPlayer) != 1:
			if iPlayer == con.iArmenia: # use modifiers of KoJ
				pPlayer.changeInflationModifier(-5)
				pPlayer.setGrowthPercent(con.tGrowthPercent[con.iCrusaders])
				pPlayer.setProductionPercent(con.tProductionPercent[con.iCrusaders])
				pPlayer.setResearchPercent(con.tResearchPercent[con.iCrusaders])
				pPlayer.setCulturePercent(con.tCulturePercent[con.iCrusaders])
				pPlayer.setEspionagePercent(con.tEspionagePercent[con.iCrusaders])
			if iPlayer == con.iGolden:
				pPlayer.changeInflationModifier(-5)
				pPlayer.setGrowthPercent(con.tGrowthPercent[con.iOttomans])
				pPlayer.setProductionPercent(con.tProductionPercent[con.iOttomans])
				pPlayer.setCulturePercent(con.tCulturePercent[con.iOttomans])
			if iPlayer == con.iRum:
				pPlayer.changeInflationModifier(-5)
				pPlayer.setGrowthPercent(con.tGrowthPercent[con.iChagatai])
				pPlayer.setProductionPercent(con.tProductionPercent[con.iMongols])
				pPlayer.setEspionagePercent(con.tEspionagePercent[con.iGolden])
			if iPlayer == con.iAlans:
				pPlayer.changeInflationModifier(-10)
				pPlayer.setGrowthPercent(con.tGrowthPercent[con.iGhorids])
				pPlayer.setProductionPercent(con.tProductionPercent[con.iTimurids])
				pPlayer.setCulturePercent(con.tCulturePercent[con.iGhorids])
				pPlayer.setResearchPercent(con.tResearchPercent[con.iGolden])
			if iPlayer == con.iKhanids:
				pPlayer.changeInflationModifier(-20)
				pPlayer.setGrowthPercent(con.tGrowthPercent[con.iTimurids])
				pPlayer.setProductionPercent(con.tProductionPercent[con.iTimurids])
				pPlayer.setCulturePercent(con.tCulturePercent[con.iTimurids])
				pPlayer.setResearchPercent(con.tResearchPercent[con.iGolden])
			if iPlayer == con.iKypchaks:
				pPlayer.changeInflationModifier(-5)
				pPlayer.setGrowthPercent(con.tGrowthPercent[con.iTimurids])
				pPlayer.setProductionPercent(con.tProductionPercent[con.iTimurids])
				pPlayer.setCulturePercent(con.tCulturePercent[con.iTimurids])
				pPlayer.setResearchPercent(con.tResearchPercent[con.iGolden])		  
			if iPlayer == con.iKhazars:
				pPlayer.changeInflationModifier(-25)
				pPlayer.setGrowthPercent(con.tGrowthPercent[con.iTimurids])
				pPlayer.setProductionPercent(con.tProductionPercent[con.iOttomans])
				pPlayer.setCulturePercent(con.tCulturePercent[con.iTimurids])
				pPlayer.setResearchPercent(con.tResearchPercent[con.iTimurids])
			if iPlayer == con.iKhitai:
				pPlayer.changeInflationModifier(-10)
				pPlayer.setGrowthPercent(con.tGrowthPercent[con.iTimurids])
				pPlayer.setProductionPercent(con.tProductionPercent[con.iOttomans])
				pPlayer.setCulturePercent(con.tCulturePercent[con.iTimurids])
				pPlayer.setResearchPercent(con.tResearchPercent[con.iTimurids])
				pPlayer.setEspionagePercent(con.tEspionagePercent[con.iChagatai])
			if iPlayer == con.iGhorids:
				pPlayer.changeInflationModifier(-10)
			if iPlayer == con.iCrusaders:
				pPlayer.changeInflationModifier(-10)
				pPlayer.setProductionPercent(con.tProductionPercent[con.iMongols])
			if iPlayer == con.iKhwarezm:
				pPlayer.changeInflationModifier(-15)
			if iPlayer == con.iSeljuks:
				pPlayer.changeInflationModifier(-10)
				pPlayer.setProductionPercent(con.tProductionPercent[con.iGolden])
				pPlayer.setGrowthPercent(con.tGrowthPercent[con.iGolden])
				pPlayer.setResearchPercent(con.tResearchPercent[con.iGolden])
				pPlayer.setCulturePercent(con.tCulturePercent[con.iGolden])
			if iPlayer in [con.iChauhan, con.iGujarat, con.iMalwa, con.iGeorgia, con.iYemen, con.iGhaznavids, con.iBuyids, con.iSindh]:
				pPlayer.changeInflationModifier(-5)
		
		sd.setCivStatus(iPlayer, 1)
		
		if iPlayer in self.respawnedNames:
			if iPlayer == con.iGhorids:
				pPlayer.setLeader(gc.getInfoTypeForString("LEADER_QUTBUDDIN"))
				pPlayer.setFlag("Art/Interface/TeamColor/FlagDECAL_Delhi.dds")
				pPlayer.setCivilizationType(gc.getInfoTypeForString("CIVILIZATION_DELHI"))
				plot = gc.getMap().plot(con.tDelhi[0], con.tDelhi[1])
				if plot.isCity():
					city = plot.getPlotCity()
					if city.getOwner() == iPlayer:
						self.setCivDesc(iPlayer, self.respawnedNames[iPlayer], "TXT_KEY_CIV_DELHI_SHORT_DESC", "TXT_KEY_CIV_DELHI_ADJECTIVE")
						pPlayer.setName(localText.getText("TXT_KEY_LEADER_QUTBUDDIN_AIBAK", ()))
						return
				if gc.getGame().getGameTurnYear() < 1320:
					self.setCivDesc(iPlayer, "TXT_KEY_CIV_KHILJI_DESC", "TXT_KEY_CIV_KHILJI_SHORT_DESC", "TXT_KEY_CIV_KHILJI_ADJECTIVE")
					pPlayer.setName(localText.getText("TXT_KEY_LEADER_KHILJI", ()))
				elif gc.getGame().getGameTurnYear() < 1414:
					self.setCivDesc(iPlayer, "TXT_KEY_CIV_TUGHLAQ_DESC", "TXT_KEY_CIV_TUGHLAQ_SHORT_DESC", "TXT_KEY_CIV_TUGHLAQ_ADJECTIVE")
					pPlayer.setName(localText.getText("TXT_KEY_LEADER_TUGHLUQ", ()))
				elif gc.getGame().getGameTurnYear() < 1451:
					self.setCivDesc(iPlayer, "TXT_KEY_CIV_SAYYID_DESC", "TXT_KEY_CIV_SAYYID_SHORT_DESC", "TXT_KEY_CIV_SAYYID_ADJECTIVE")
					pPlayer.setName(localText.getText("TXT_KEY_LEADER_SAYYID", ()))
				else:
					self.setCivDesc(iPlayer, "TXT_KEY_CIV_LODI_DESC", "TXT_KEY_CIV_TUGHLAQ_LODI_DESC", "TXT_KEY_CIV_LODI_ADJECTIVE")
					pPlayer.setName(localText.getText("TXT_KEY_LEADER_LODI", ()))
			elif iPlayer == con.iChagatai:
				pPlayer.setCivilizationType(gc.getInfoTypeForString("CIVILIZATION_MOGHULS"))
				if gc.getGame().getGameTurnYear() < 1530:
					self.setCivDesc(iPlayer, self.respawnedNames[iPlayer], "TXT_KEY_CIV_MOG_SHORT_DESC", "TXT_KEY_CIV_MOG_ADJECTIVE")
					pPlayer.setName(localText.getText("TXT_KEY_LEADER_UWAISK", ()))
				else:
					self.setCivDesc(iPlayer, "TXT_KEY_CIV_YARK_DESC_DEFAULT", "TXT_KEY_CIV_MOG_SHORT_DESC", "TXT_KEY_CIV_MOG_ADJECTIVE")
					pPlayer.setName(localText.getText("TXT_KEY_LEADER_ABDUR", ()))
			elif iPlayer == con.iMongols:
				self.setCivDesc(iPlayer, self.respawnedNames[iPlayer], "TXT_KEY_CIV_JALAYIR_SHORT_DESC")
				pPlayer.setLeader(gc.getInfoTypeForString("LEADER_JALAY"))
				pPlayer.setCivilizationType(gc.getInfoTypeForString("CIVILIZATION_JALAYIR"))
			elif iPlayer == con.iSeljuks:
				self.setCivDesc(iPlayer, self.respawnedNames[iPlayer], "TXT_KEY_CIV_KARA_SHORT_DESC")
				pPlayer.setLeader(gc.getInfoTypeForString("LEADER_ISKANDER"))
				pPlayer.setCivilizationType(gc.getInfoTypeForString("CIVILIZATION_KARA"))
			elif iPlayer == con.iBahmanids:
				self.setCivDesc(iPlayer, self.respawnedNames[iPlayer], "TXT_KEY_CIV_BIJ_SHORT_DESC", "TXT_KEY_CIV_BIJ_ADJECTIVE")
				pPlayer.setName(localText.getText("TXT_KEY_LEADER_ISMADIL", ()))			
			elif iPlayer == con.iChalukya:
				self.setCivDesc(iPlayer, self.respawnedNames[iPlayer], "TXT_KEY_CIV_SEUNA_SHORT_DESC", "TXT_KEY_CIV_SEUNA_ADJECTIVE")
				pPlayer.setName(localText.getText("TXT_KEY_LEADER_SIMHANA", ()))
			elif iPlayer == con.iKiev:
				self.setCivDesc(iPlayer, self.respawnedNames[iPlayer], "TXT_KEY_CIV_KIEV_SHORT_DESC", "TXT_KEY_CIV_KIEV_ADJECTIVE")
				pPlayer.setName(localText.getText("TXT_KEY_LEADER_SIMEONO", ()))
			elif iPlayer == con.iGhaznavids:
				self.setCivDesc(iPlayer, self.respawnedNames[iPlayer], "TXT_KEY_CIV_KARTIDS_SHORT_DESC")
				pPlayer.setLeader(gc.getInfoTypeForString("LEADER_SHAMSUD"))
				pPlayer.setCivilizationType(gc.getInfoTypeForString("CIVILIZATION_KARTIDS"))
			elif iPlayer == con.iBuyids:
				self.setCivDesc(iPlayer, self.respawnedNames[iPlayer], "TXT_KEY_CIV_MUZZ_SHORT_DESC")
				pPlayer.setLeader(gc.getInfoTypeForString("LEADER_MUBARIZ"))
				pPlayer.setCivilizationType(gc.getInfoTypeForString("CIVILIZATION_MUZZ"))
			elif iPlayer == con.iChauhan:
				self.setCivDesc(iPlayer, self.respawnedNames[iPlayer], "TXT_KEY_CIV_MEWAR_SHORT_DESC", "TXT_KEY_CIV_MEWAR_ADJECTIVE")
				pPlayer.setName(localText.getText("TXT_KEY_LEADER_MAHARANA_PRATAP", ()))
			elif iPlayer == con.iRum:
				self.setCivDesc(iPlayer, self.respawnedNames[iPlayer], "TXT_KEY_CIV_KARAMAN_SHORT_DESC")
				pPlayer.setName(localText.getText("TXT_KEY_LEADER_KARAMAN", ()))
				pPlayer.setFlag("Art/Interface/TeamColor/FlagDECAL_Karaman.dds")
				pPlayer.setCivilizationType(gc.getInfoTypeForString("CIVILIZATION_KARAMAN"))
			elif iPlayer == con.iKhazars:
				self.setCivDesc(iPlayer, self.respawnedNames[iPlayer], "TXT_KEY_CIV_KALMYK_SHORT_DESC")
				pPlayer.setName(localText.getText("TXT_KEY_LEADER_AYUKA", ()))
				#pPlayer.setFlag("Art/Interface/TeamColor/kalmyk.dds")
				pPlayer.setCivilizationType(gc.getInfoTypeForString("CIVILIZATION_KALMYK"))
			elif iPlayer == con.iAlans:
				self.setCivDesc(iPlayer, self.respawnedNames[iPlayer], "TXT_KEY_CIV_CIRCASSIA_SHORT_DESC")
				pPlayer.setName(localText.getText("TXT_KEY_LEADER_INAL", ()))
				pPlayer.setFlag("Art/Interface/TeamColor/circassian.dds")	   
				pPlayer.setCivilizationType(gc.getInfoTypeForString("CIVILIZATION_CIRCASSIA"))
			elif iPlayer == con.iKypchaks:
				self.setCivDesc(iPlayer, self.respawnedNames[iPlayer], "TXT_KEY_CIV_NOGAI_SHORT_DESC")
				pPlayer.setName(localText.getText("TXT_KEY_LEADER_MUSABEY", ()))
				pPlayer.setFlag("Art/Interface/TeamColor/nogai.dds")		
				pPlayer.setCivilizationType(gc.getInfoTypeForString("CIVILIZATION_NOGAI"))
			elif iPlayer == con.iKhitai:
				self.setCivDesc(iPlayer, self.respawnedNames[iPlayer], "TXT_KEY_CIV_ZUNGHAR_SHORT_DESC")
				pPlayer.setLeader(gc.getInfoTypeForString("LEADER_ZHU"))
				#pPlayer.setFlag("Art/Interface/TeamColor/zhungar.dds")
				pPlayer.setCivilizationType(gc.getInfoTypeForString("CIVILIZATION_ZUNGHAR"))		  
			elif iPlayer == con.iCrusaders:
				self.setCivDesc(iPlayer, self.respawnedNames[iPlayer], "TXT_KEY_CIV_CYPRUS_SHORT_DESC")
				pPlayer.setLeader(gc.getInfoTypeForString("LEADER_GUY"))
				pPlayer.setName(localText.getText("TXT_KEY_LEADER_GUY", ()))
			elif iPlayer == con.iKhwarezm:
				self.setCivDesc(iPlayer, self.respawnedNames[iPlayer], "TXT_KEY_CIV_SHAYBANIDS_SHORT_DESC")
				pPlayer.setName(localText.getText("TXT_KEY_LEADER_SHAYBANI", ()))
				pPlayer.setFlag("Art/Interface/TeamColor/FlagDECAL_Khiva.dds")
				pPlayer.setCivilizationType(gc.getInfoTypeForString("CIVILIZATION_SHAYBANIDS"))
			elif iPlayer == con.iGolden:
				self.setCivDesc(iPlayer, self.respawnedNames[iPlayer], "TXT_KEY_CIV_CRIMEAN_SHORT_DESC")
				pPlayer.setName(localText.getText("TXT_KEY_LEADER_SAHIB_GIRAY", ()))
				pPlayer.setFlag("Art/Interface/TeamColor/Crimean.dds")	  
				pPlayer.setCivilizationType(gc.getInfoTypeForString("CIVILIZATION_CRIMEA"))
			elif iPlayer == con.iKhanids:
				self.setCivDesc(iPlayer, self.respawnedNames[iPlayer], "TXT_KEY_CIV_KAZAK_SHORT_DESC")
				pPlayer.setLeader(gc.getInfoTypeForString("LEADER_HAQNAZAR"))
				pPlayer.setFlag("Art/Interface/TeamColor/kazak.dds")
				pPlayer.setCivilizationType(gc.getInfoTypeForString("CIVILIZATION_KAZAK"))
			elif iPlayer == con.iArmenia:
				self.setCivDesc(iPlayer, self.respawnedNames[iPlayer])
				pPlayer.setName(localText.getText("TXT_KEY_LEADER_LEVON", ()))
				pPlayer.setFlag("Art/Interface/TeamColor/FlagDECAL_Cilicia.dds")
				pPlayer.setCivilizationType(gc.getInfoTypeForString("CIVILIZATION_CILICIA"))
			else:
				self.setCivDesc(iPlayer, self.respawnedNames[iPlayer])
			
				
	def onVassalState(self, argsList):
		iMaster, iVassal, bVassal = argsList
		self.checkName(iVassal)
	
	
	def onPlayerChangeStateReligion(self, argsList):
		iPlayer, iNewReligion, iOldReligion = argsList
		self.checkName(iPlayer)


	def onRevolution(self, iPlayer):
		self.checkName(iPlayer)
		

	def onCityAcquired(self, argsList):
		iPreviousOwner, iNewOwner, city, bConquest, bTrade = argsList
		
		self.checkName(iPreviousOwner)
		self.checkName(iNewOwner)