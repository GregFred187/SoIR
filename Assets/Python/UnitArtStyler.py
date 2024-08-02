# UnitArtStyler by edead
# Works only with the related DLL changes (CvUnit::setArtDefineTag and CvUnitInfo::getArtDefineTag)
# Use to convert unit art of independent units based on the city art style, or province, or w/e

from CvPythonExtensions import *
import Consts as con

gc = CyGlobalContext()

# Unit Art Styles for a particular city/plot Art Style
g_CityArtStyles = (
"UNIT_ARTSTYLE_MIDDLE_EAST", 		# 0 = ARTSTYLE_EUROPEAN (not used)
"UNIT_ARTSTYLE_GENERIC_ARABIAN", 	# 1 = ARTSTYLE_ARABIAN (Egypt, Syria, Iraq, Arabia)
"UNIT_ARTSTYLE_MIDDLE_EAST", 		# 2 = ARTSTYLE_MIDDLE_EAST (Iran, Afghanistan and Pakistan, default style)
"UNIT_ARTSTYLE_MIDDLE_EAST",		# 3 = ARTSTYLE_MEDITERRANEAN (Anatolia & Caucasus)
"UNIT_ARTSTYLE_GENERIC_INDIAN",		# 4 = ARTSTYLE_INDIAN
"UNIT_ARTSTYLE_GENERIC_TURKISH",	# 5 = ARTSTYLE_TURKISH
"UNIT_ARTSTYLE_GENERIC_AFRICAN",	# 6 = ARTSTYLE_DESERT (Nubia)
)

# Unit Art Styles for a particular region (province)
g_RegionArtStyles = {
	con.rGeorgia 			: "UNIT_ARTSTYLE_GEORGIAN",
	con.rGreaterArmenia		: "UNIT_ARTSTYLE_ARMENIAN",
	con.rKars				: "UNIT_ARTSTYLE_ARMENIAN",
	con.rVaspurakan			: "UNIT_ARTSTYLE_ARMENIAN",
	con.rEdessa				: "UNIT_ARTSTYLE_ARMENIAN",
	con.rThrace				: "UNIT_ARTSTYLE_BYZANTINE",
	con.rRhodes				: "UNIT_ARTSTYLE_BYZANTINE",
	con.rCyprus				: "UNIT_ARTSTYLE_BYZANTINE",
	con.rAsia				: "UNIT_ARTSTYLE_BYZANTINE",
	con.rBithynia			: "UNIT_ARTSTYLE_BYZANTINE",
	con.rLycia				: "UNIT_ARTSTYLE_BYZANTINE",
	con.rPontus				: "UNIT_ARTSTYLE_BYZANTINE",
	con.rGalatia			: "UNIT_ARTSTYLE_BYZANTINE",
	con.rPaphlagonia		: "UNIT_ARTSTYLE_BYZANTINE",
	con.rCilicia			: "UNIT_ARTSTYLE_BYZANTINE",
	con.rCappadocia			: "UNIT_ARTSTYLE_BYZANTINE",
	con.rLesserArmenia		: "UNIT_ARTSTYLE_BYZANTINE",
	con.rTrebizond			: "UNIT_ARTSTYLE_BYZANTINE",
	con.rHindukush			: "UNIT_ARTSTYLE_AFGHAN",
	con.rGandhar			: "UNIT_ARTSTYLE_AFGHAN",
	con.rSindh				: "UNIT_ARTSTYLE_SINDH",
	con.rPunjab				: "UNIT_ARTSTYLE_SINDH",
	con.rSyria				: "UNIT_ARTSTYLE_SYRIAN",
	con.rNorthernSyria		: "UNIT_ARTSTYLE_SYRIAN",
	con.rPalestine			: "UNIT_ARTSTYLE_SYRIAN",
	con.rGujarat			: "UNIT_ARTSTYLE_GENERIC_INDIAN",
	con.rMaharashtra		: "UNIT_ARTSTYLE_GENERIC_INDIAN",
	con.rGoa				: "UNIT_ARTSTYLE_GENERIC_INDIAN",
}

# Conditional Unit Art Styles for a particular region : (iDate, tReligions, eArtStyle)
g_ConditionalArtStyles = {
	con.rCilicia			: (con.tRespawn[con.iArmenia], (con.iOrthodoxy), "UNIT_ARTSTYLE_ARMENIAN"),
	con.rAsia				: (con.tBirth[con.iRum], (con.iSunni, con.iShia), "UNIT_ARTSTYLE_GENERIC_TURKISH"),
	con.rBithynia			: (con.tBirth[con.iRum], (con.iSunni, con.iShia), "UNIT_ARTSTYLE_GENERIC_TURKISH"),
	con.rLycia				: (con.tBirth[con.iRum], (con.iSunni, con.iShia), "UNIT_ARTSTYLE_GENERIC_TURKISH"),
	con.rPontus				: (con.tBirth[con.iRum], (con.iSunni, con.iShia), "UNIT_ARTSTYLE_GENERIC_TURKISH"),
	con.rGalatia			: (con.tBirth[con.iRum], (con.iSunni, con.iShia), "UNIT_ARTSTYLE_GENERIC_TURKISH"),
	con.rPaphlagonia		: (con.tBirth[con.iRum], (con.iSunni, con.iShia), "UNIT_ARTSTYLE_GENERIC_TURKISH"),
	con.rCilicia			: (con.tBirth[con.iRum], (con.iSunni, con.iShia), "UNIT_ARTSTYLE_GENERIC_TURKISH"),
	con.rCappadocia			: (con.tBirth[con.iRum], (con.iSunni, con.iShia), "UNIT_ARTSTYLE_GENERIC_TURKISH"),
	con.rLesserArmenia		: (con.tBirth[con.iRum], (con.iSunni, con.iShia), "UNIT_ARTSTYLE_GENERIC_TURKISH"),
	con.rKerman				: (con.tBirth[con.iSeljuks], (), "UNIT_ARTSTYLE_GENERIC_TURKISH"),
	con.rFars				: (con.tBirth[con.iSeljuks], (), "UNIT_ARTSTYLE_GENERIC_TURKISH"),
	con.rYazd				: (con.tBirth[con.iSeljuks], (), "UNIT_ARTSTYLE_GENERIC_TURKISH"),
	con.rHormuz				: (con.tBirth[con.iSeljuks], (), "UNIT_ARTSTYLE_GENERIC_TURKISH"),
	con.rLuristan			: (con.tBirth[con.iSeljuks], (), "UNIT_ARTSTYLE_GENERIC_TURKISH"),
	con.rKurdistan			: (con.tBirth[con.iSeljuks], (), "UNIT_ARTSTYLE_GENERIC_TURKISH"),
	con.rJibal				: (con.tBirth[con.iSeljuks], (), "UNIT_ARTSTYLE_GENERIC_TURKISH"),
	con.rWesternKhorasan	: (con.tBirth[con.iSeljuks], (), "UNIT_ARTSTYLE_GENERIC_TURKISH"),
	con.rEasternKhorasan	: (con.tBirth[con.iSeljuks], (), "UNIT_ARTSTYLE_GENERIC_TURKISH"),
	con.rGhazni				: (con.tBirth[con.iGhaznavids], (), "UNIT_ARTSTYLE_GENERIC_TURKISH"),
	con.rKandahar			: (con.tBirth[con.iGhaznavids], (), "UNIT_ARTSTYLE_GENERIC_TURKISH"),
	con.rUttarBharat		: (con.tRespawn[con.iGhorids], (con.iSunni, con.iShia), "UNIT_ARTSTYLE_AFGHAN"),
	con.rPunjab				: (con.tRespawn[con.iGhorids], (con.iSunni, con.iShia), "UNIT_ARTSTYLE_AFGHAN"),
}


def checkUnitArt(unit):
	"""Checks unit and either updates or resets the ArtDefineTag."""
	if unit:
		if gc.getPlayer(unit.getOwner()).isMinorCiv():
			updateUnitArt(unit)
		else:
			resetUnitArt(unit)

			
def setUnitArt(unit, eUnitArtStyle):
	"""Sets the ArtDefineTag of unit based on eArtStyle (not UnitArtStyle!)."""
	if unit and eUnitArtStyle >= 0:
		unit.setArtDefineTag(gc.getUnitInfo(unit.getUnitType()).getArtDefineTag(0, eUnitArtStyle))


def updateUnitArt(unit):
	"""Updates the ArtDefineTag of unit based on the ArtStyle of its plot or region (province)."""
	if unit:
		plot = unit.plot()
		if plot:
			# base art style from plot art
			eUnitArtStyle = -1
			if plot.getArtStyleType() >= 0 and plot.getArtStyleType() < len(g_CityArtStyles):
				eUnitArtStyle = gc.getInfoTypeForString(g_CityArtStyles[plot.getArtStyleType()])
			# art style change based on date and religions present in city
			if plot.getRegionID() in g_ConditionalArtStyles:
				if gc.getGame().getGameTurnYear() >= g_ConditionalArtStyles[plot.getRegionID()][0]:
					bFound = True
					if plot.isCity():
						city = plot.getPlotCity()
						bFound = False
						for iReligion in g_ConditionalArtStyles[plot.getRegionID()][1]:
							if city.isHasReligion(iReligion):
								bFound = True
								break
					if bFound:
						eUnitArtStyle = gc.getInfoTypeForString(g_ConditionalArtStyles[plot.getRegionID()][2])
			setUnitArt(unit, eUnitArtStyle)


def updateUnitArtAtPlot(plot):
	"""Updates the ArtDefineTag of all units at a given plot."""
	if plot:
		for i in range(plot.getNumUnits()):
			updateUnitArt(plot.getUnit(i))


def resetUnitArt(unit):
	"""Resets the ArtDefineTag, bringing back the default civ-based UnitArtStyle."""
	if unit:
		unit.setArtDefineTag("")
