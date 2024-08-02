#include "CvGameCoreDLL.h"
#include "CyPlayer.h"
#include "CyUnit.h"
#include "CyCity.h"
#include "CyPlot.h"
#include "CySelectionGroup.h"
#include "CyArea.h"
//# include <boost/python/manage_new_object.hpp>
//# include <boost/python/return_value_policy.hpp>
//# include <boost/python/scope.hpp>

//
// published python interface for CyPlayer
//

void CyPlayerPythonInterface2(python::class_<CyPlayer>& x)
{
	OutputDebugString("Python Extension Module - CyPlayerPythonInterface2\n");

	// set the docstring of the current module scope 
	python::scope().attr("__doc__") = "Civilization IV Player Class"; 
	x
		.def("AI_updateFoundValues", &CyPlayer::AI_updateFoundValues, "void (bool bStartingLoc)")
		.def("AI_foundValue", &CyPlayer::AI_foundValue, "int (int, int, int, bool)")
		.def("AI_isFinancialTrouble", &CyPlayer::AI_isFinancialTrouble, "bool ()")
		.def("AI_demandRebukedWar", &CyPlayer::AI_demandRebukedWar, "bool (int /*PlayerTypes*/)")
		.def("AI_getAttitude", &CyPlayer::AI_getAttitude, "AttitudeTypes (int /*PlayerTypes*/) - Gets the attitude of the player towards the player passed in")
		.def("AI_unitValue", &CyPlayer::AI_unitValue, "int (int /*UnitTypes*/ eUnit, int /*UnitAITypes*/ eUnitAI, CyArea* pArea)")
		.def("AI_civicValue", &CyPlayer::AI_civicValue, "int (int /*CivicTypes*/ eCivic)")
		.def("AI_totalUnitAIs", &CyPlayer::AI_totalUnitAIs, "int (int /*UnitAITypes*/ eUnitAI)")
		.def("AI_totalAreaUnitAIs", &CyPlayer::AI_totalAreaUnitAIs, "int (CyArea* pArea, int /*UnitAITypes*/ eUnitAI)")
		.def("AI_totalWaterAreaUnitAIs", &CyPlayer::AI_totalWaterAreaUnitAIs, "int (CyArea* pArea, int /*UnitAITypes*/ eUnitAI)")
		.def("AI_getNumAIUnits", &CyPlayer::AI_getNumAIUnits, "int (UnitAIType) - Returns # of UnitAITypes the player current has of UnitAIType")
		.def("AI_getAttitudeExtra", &CyPlayer::AI_getAttitudeExtra, "int (int /*PlayerTypes*/ eIndex) - Returns the extra attitude for this player - usually scenario specific")
		.def("AI_setAttitudeExtra", &CyPlayer::AI_setAttitudeExtra, "void (int /*PlayerTypes*/ eIndex, int iNewValue) - Sets the extra attitude for this player - usually scenario specific")
		.def("AI_changeAttitudeExtra", &CyPlayer::AI_changeAttitudeExtra, "void (int /*PlayerTypes*/ eIndex, int iChange) - Changes the extra attitude for this player - usually scenario specific")
		.def("AI_getMemoryCount", &CyPlayer::AI_getMemoryCount, "int (/*PlayerTypes*/ eIndex1, /*MemoryTypes*/ eIndex2)")
		.def("AI_changeMemoryCount", &CyPlayer::AI_changeMemoryCount, "void (/*PlayerTypes*/ eIndex1, /*MemoryTypes*/ eIndex2, int iChange)")
		.def("AI_getExtraGoldTarget", &CyPlayer::AI_getExtraGoldTarget, "int ()")
		.def("AI_setExtraGoldTarget", &CyPlayer::AI_setExtraGoldTarget, "void (int)")

		.def("getScoreHistory", &CyPlayer::getScoreHistory, "int (int iTurn)")
		.def("getEconomyHistory", &CyPlayer::getEconomyHistory, "int (int iTurn)")
		.def("getIndustryHistory", &CyPlayer::getIndustryHistory, "int (int iTurn)")
		.def("getAgricultureHistory", &CyPlayer::getAgricultureHistory, "int (int iTurn)")
		.def("getPowerHistory", &CyPlayer::getPowerHistory, "int (int iTurn)")
		.def("getCultureHistory", &CyPlayer::getCultureHistory, "int (int iTurn)")
		.def("getEspionageHistory", &CyPlayer::getEspionageHistory, "int (int iTurn)")

		.def("getScriptData", &CyPlayer::getScriptData, "str () - Get stored custom data (via pickle)")
		.def("setScriptData", &CyPlayer::setScriptData, "void (str) - Set stored custom data (via pickle)")

		.def("chooseTech", &CyPlayer::chooseTech, "void (int iDiscover, wstring szText, bool bFront)")

		.def("AI_maxGoldTrade", &CyPlayer::AI_maxGoldTrade, "int (int)")
		.def("AI_maxGoldPerTurnTrade", &CyPlayer::AI_maxGoldPerTurnTrade, "int (int)")

		.def("splitEmpire", &CyPlayer::splitEmpire, "bool (int iAreaId)")
		.def("canSplitEmpire", &CyPlayer::canSplitEmpire, "bool ()")
		.def("canSplitArea", &CyPlayer::canSplitArea, "bool (int)")
		.def("canHaveTradeRoutesWith", &CyPlayer::canHaveTradeRoutesWith, "bool (int)")
		.def("forcePeace", &CyPlayer::forcePeace, "void (int)")
		
		// edead: start
		.def("setFlag", &CyPlayer::setFlag, "void (str s)") //Rhye
		.def("setLeader", &CyPlayer::setLeader, "void (int i)") //Rhye
		.def("getLeader", &CyPlayer::getLeader, "int /*LeaderHeadTypes*/ ()") //Rhye
		
		.def("getBorders", &CyPlayer::getBorders, "int (int ePlayer)")
		.def("setBorders", &CyPlayer::setBorders, "void (int ePlayer, int iNewValue)")
		.def("getAttitudeModifier", &CyPlayer::getAttitudeModifier, "int (int ePlayer)")
		.def("setAttitudeModifier", &CyPlayer::setAttitudeModifier, "void (int ePlayer, int iNewValue)")
		.def("getDiplomacyModifier", &CyPlayer::getDiplomacyModifier, "int ()")
		.def("changeDiplomacyModifier", &CyPlayer::changeDiplomacyModifier, "void (int iChange)")
		.def("getLuck", &CyPlayer::getLuck, "int ()")
		.def("setLuck", &CyPlayer::setLuck, "void (int iNewValue)")
		.def("setStartYear", &CyPlayer::setStartYear, "void (int iNewValue)")
		.def("changeInflationModifier", &CyPlayer::changeInflationModifier, "void (int iChange)")
		.def("setGrowthPercent", &CyPlayer::setGrowthPercent, "void (int iNewValue)")
		.def("setProductionPercent", &CyPlayer::setProductionPercent, "void (int iNewValue)")
		.def("setResearchPercent", &CyPlayer::setResearchPercent, "void (int iNewValue)")
		.def("setCulturePercent", &CyPlayer::setCulturePercent, "void (int iNewValue)")
		.def("setEspionagePercent", &CyPlayer::setEspionagePercent, "void (int iNewValue)")
		.def("setGreatPeoplePercent", &CyPlayer::setGreatPeoplePercent, "void (int iNewValue)")
		.def("setReligionSpreadPercent", &CyPlayer::setReligionSpreadPercent, "void (int /*ReligionTypes*/ eIndex, int iNewValue)")
		.def("changeInflationModifier", &CyPlayer::changeInflationModifier, "void (int iChange)")
		.def("changeDistanceMaintenanceModifier", &CyPlayer::changeDistanceMaintenanceModifier, "void (int iChange)")
		.def("changeNumCitiesMaintenanceModifier", &CyPlayer::changeNumCitiesMaintenanceModifier, "void (int iChange)")
		
		.def("AI_getCompactEmpireModifier", &CyPlayer::AI_getCompactEmpireModifier, "int ()")
		.def("AI_setCompactEmpireModifier", &CyPlayer::AI_setCompactEmpireModifier, "void (int)")
		.def("AI_getMassacreProb", &CyPlayer::AI_getMassacreProb, "int ()")
		.def("AI_setMassacreProb", &CyPlayer::AI_setMassacreProb, "void (int)")
		.def("AI_getBuildPersecutorProb", &CyPlayer::AI_getBuildPersecutorProb, "int ()")
		.def("AI_setBuildPersecutorProb", &CyPlayer::AI_setBuildPersecutorProb, "void (int)")
		.def("AI_getWarDistanceModifier", &CyPlayer::AI_getWarDistanceModifier, "int ()")
		.def("AI_setWarDistanceModifier", &CyPlayer::AI_setWarDistanceModifier, "void (int)")
		.def("AI_getWarCoastalModifier", &CyPlayer::AI_getWarCoastalModifier, "int ()")
		.def("AI_setWarCoastalModifier", &CyPlayer::AI_setWarCoastalModifier, "void (int)")
		.def("AI_getMaxTakenTiles", &CyPlayer::AI_getMaxTakenTiles, "int ()")
		.def("AI_setMaxTakenTiles", &CyPlayer::AI_setMaxTakenTiles, "void (int)")
		.def("AI_getUnitAIModifier", &CyPlayer::AI_getUnitAIModifier, "int (int)")
		.def("AI_setUnitAIModifier", &CyPlayer::AI_setUnitAIModifier, "void (int, int)")
		// edead: end

		;
}
