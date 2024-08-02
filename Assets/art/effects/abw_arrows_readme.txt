BOWMAN ARROWS MANAGEMENT

If you wish to preserve the right kind of arrow during combat animation sequence, you must:

1) append the following code into your modded CIV4EffectInfos.xml, editing the <Path> rows below:

		<!-- longbowman arrows:-->
		<EffectInfo>
			<Type>EFFECT_LONGBOWARROW1</Type>
			<Description>Longbow Arrow</Description>
			<fScale>1.0</fScale>
			<fUpdateRate>1.0</fUpdateRate>
			<Path>[...your path...]/anim_effects/abw_arrow1.nif</Path>
			<bIsProjectile>1</bIsProjectile>
			<fSpeed>500.0</fSpeed>
			<fArcValue>0.0</fArcValue>
		</EffectInfo>
		<EffectInfo>
			<Type>EFFECT_LONGBOWARROW2</Type>
			<Description>Longbow Arrow</Description>
			<fScale>1.0</fScale>
			<fUpdateRate>1.0</fUpdateRate>
			<Path>[...your path...]/anim_effects/abw_arrow2.nif</Path>
			<bIsProjectile>1</bIsProjectile>
			<fSpeed>500.0</fSpeed>
			<fArcValue>0.0</fArcValue>
		</EffectInfo>

2) address the right kind of kfm into <KFM> rows of your modded CIV4ArtDefines_Unit.xml as follow:

for bowmen using light brown arrows:
			<KFM>[...your path...]/anim/longbowman_1.kfm</KFM>
 
for bowmen using dark brown arrows:
			<KFM>[...your path...]/anim/longbowman_2.kfm</KFM>
 
During combat sequence, each modded #_kfm calls its rangedstrik#.kf animation, each #.kf calls its EFFECT_XXX xml <Type>, each EFFECT_XXX calls its effect-nif properly.
 