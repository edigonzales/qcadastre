<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="2.1.0-Master" minimumScale="-4.65661e-10" maximumScale="20000" minLabelScale="1" maxLabelScale="1e+08" hasScaleBasedVisibilityFlag="1" scaleBasedLabelVisibilityFlag="0">
  <renderer-v2 symbollevels="0" type="RuleRenderer">
    <rules>
      <rule filter="&quot;art&quot;  = 23" symbol="0" label="Ruine_archaelogisches_Objekt"/>
      <rule filter="&quot;art&quot;  = 30" symbol="1" label="Hochspannungsfreileitung"/>
      <rule filter="&quot;art&quot;  = 31" symbol="2" label="Druckleitung"/>
      <rule filter="&quot;art&quot;  = 34" symbol="3" label="Luftseilbahn"/>
      <rule filter="&quot;art&quot;  = 35" symbol="4" label="Gondelbahn_Sesselbahn"/>
      <rule filter="&quot;art&quot;  = 36" symbol="5" label="Materialseilbahn"/>
      <rule filter="&quot;art&quot;  = 37" symbol="6" label="Skilift"/>
      <rule filter="&quot;art&quot;  = 38" symbol="7" label="Faehre"/>
      <rule filter="&quot;art&quot;  = 40" symbol="8" label="Achse"/>
      <rule filter="&quot;art&quot;  = 17" symbol="9" label="Mast_Leitung"/>
      <rule scalemaxdenom="5000" filter="&quot;art&quot;  NOT IN (23,30,31,34,35,36,37,38,40,17)" symbol="10" label="andere"/>
    </rules>
    <symbols>
      <symbol alpha="1" type="line" name="0">
        <layer pass="0" class="SimpleLine" locked="0">
          <prop k="capstyle" v="square"/>
          <prop k="color" v="255,0,0,255"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="solid"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.4"/>
          <prop k="width_unit" v="MM"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="1">
        <layer pass="0" class="SimpleLine" locked="0">
          <prop k="capstyle" v="square"/>
          <prop k="color" v="244,28,241,255"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="dash dot dot"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.4"/>
          <prop k="width_unit" v="MM"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="10">
        <layer pass="0" class="SimpleLine" locked="0">
          <prop k="capstyle" v="flat"/>
          <prop k="color" v="126,126,126,255"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="miter"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="dash"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.35"/>
          <prop k="width_unit" v="MM"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="2">
        <layer pass="0" class="SimpleLine" locked="0">
          <prop k="capstyle" v="flat"/>
          <prop k="color" v="0,255,255,255"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="miter"/>
          <prop k="offset" v="-0.5"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="dash"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.3"/>
          <prop k="width_unit" v="MM"/>
        </layer>
        <layer pass="0" class="SimpleLine" locked="0">
          <prop k="capstyle" v="flat"/>
          <prop k="color" v="0,255,255,255"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0.5"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="dash"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.3"/>
          <prop k="width_unit" v="MM"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="3">
        <layer pass="0" class="SimpleLine" locked="0">
          <prop k="capstyle" v="flat"/>
          <prop k="color" v="255,85,0,255"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="miter"/>
          <prop k="offset" v="-0.5"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="dash"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.3"/>
          <prop k="width_unit" v="MM"/>
        </layer>
        <layer pass="0" class="SimpleLine" locked="0">
          <prop k="capstyle" v="flat"/>
          <prop k="color" v="255,85,0,255"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0.5"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="dash"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.3"/>
          <prop k="width_unit" v="MM"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="4">
        <layer pass="0" class="SimpleLine" locked="0">
          <prop k="capstyle" v="flat"/>
          <prop k="color" v="0,255,127,255"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="miter"/>
          <prop k="offset" v="-0.5"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="dash"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.3"/>
          <prop k="width_unit" v="MM"/>
        </layer>
        <layer pass="0" class="SimpleLine" locked="0">
          <prop k="capstyle" v="flat"/>
          <prop k="color" v="0,255,127,255"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0.5"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="dash"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.3"/>
          <prop k="width_unit" v="MM"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="5">
        <layer pass="0" class="SimpleLine" locked="0">
          <prop k="capstyle" v="flat"/>
          <prop k="color" v="255,255,0,255"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="miter"/>
          <prop k="offset" v="-0.5"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="dash"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.3"/>
          <prop k="width_unit" v="MM"/>
        </layer>
        <layer pass="0" class="SimpleLine" locked="0">
          <prop k="capstyle" v="flat"/>
          <prop k="color" v="255,255,0,255"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0.5"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="dash"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.3"/>
          <prop k="width_unit" v="MM"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="6">
        <layer pass="0" class="SimpleLine" locked="0">
          <prop k="capstyle" v="flat"/>
          <prop k="color" v="170,0,255,255"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="miter"/>
          <prop k="offset" v="-0.5"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="dash"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.3"/>
          <prop k="width_unit" v="MM"/>
        </layer>
        <layer pass="0" class="SimpleLine" locked="0">
          <prop k="capstyle" v="flat"/>
          <prop k="color" v="170,0,255,255"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0.5"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="dash"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.3"/>
          <prop k="width_unit" v="MM"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="7">
        <layer pass="0" class="MarkerLine" locked="0">
          <prop k="interval" v="3"/>
          <prop k="interval_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="placement" v="interval"/>
          <prop k="rotate" v="1"/>
          <symbol alpha="1" type="marker" name="@7@0">
            <layer pass="0" class="SimpleMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="0,255,255,255"/>
              <prop k="color_border" v="0,255,255,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="name" v="circle"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="area"/>
              <prop k="size" v="0.8"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="8">
        <layer pass="0" class="SimpleLine" locked="0">
          <prop k="capstyle" v="square"/>
          <prop k="color" v="255,170,0,255"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="dash dot"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.4"/>
          <prop k="width_unit" v="MM"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="9">
        <layer pass="0" class="SimpleLine" locked="0">
          <prop k="capstyle" v="square"/>
          <prop k="color" v="255,0,255,255"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="dash"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.4"/>
          <prop k="width_unit" v="MM"/>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <customproperties>
    <property key="labeling" value="pal"/>
    <property key="labeling/addDirectionSymbol" value="false"/>
    <property key="labeling/angleOffset" value="0"/>
    <property key="labeling/blendMode" value="0"/>
    <property key="labeling/bufferBlendMode" value="0"/>
    <property key="labeling/bufferColorA" value="255"/>
    <property key="labeling/bufferColorB" value="255"/>
    <property key="labeling/bufferColorG" value="255"/>
    <property key="labeling/bufferColorR" value="255"/>
    <property key="labeling/bufferDraw" value="true"/>
    <property key="labeling/bufferJoinStyle" value="64"/>
    <property key="labeling/bufferNoFill" value="false"/>
    <property key="labeling/bufferSize" value="1"/>
    <property key="labeling/bufferSizeInMapUnits" value="false"/>
    <property key="labeling/bufferTransp" value="0"/>
    <property key="labeling/centroidWhole" value="false"/>
    <property key="labeling/decimals" value="0"/>
    <property key="labeling/displayAll" value="false"/>
    <property key="labeling/dist" value="0"/>
    <property key="labeling/distInMapUnits" value="false"/>
    <property key="labeling/enabled" value="false"/>
    <property key="labeling/fieldName" value=""/>
    <property key="labeling/fontBold" value="false"/>
    <property key="labeling/fontCapitals" value="0"/>
    <property key="labeling/fontFamily" value="Ubuntu"/>
    <property key="labeling/fontItalic" value="false"/>
    <property key="labeling/fontLetterSpacing" value="0"/>
    <property key="labeling/fontLimitPixelSize" value="false"/>
    <property key="labeling/fontMaxPixelSize" value="10000"/>
    <property key="labeling/fontMinPixelSize" value="3"/>
    <property key="labeling/fontSize" value="10"/>
    <property key="labeling/fontSizeInMapUnits" value="false"/>
    <property key="labeling/fontStrikeout" value="false"/>
    <property key="labeling/fontUnderline" value="false"/>
    <property key="labeling/fontWeight" value="50"/>
    <property key="labeling/fontWordSpacing" value="0"/>
    <property key="labeling/formatNumbers" value="false"/>
    <property key="labeling/isExpression" value="false"/>
    <property key="labeling/labelOffsetInMapUnits" value="true"/>
    <property key="labeling/labelPerPart" value="false"/>
    <property key="labeling/leftDirectionSymbol" value="&lt;"/>
    <property key="labeling/limitNumLabels" value="false"/>
    <property key="labeling/maxCurvedCharAngleIn" value="20"/>
    <property key="labeling/maxCurvedCharAngleOut" value="-20"/>
    <property key="labeling/maxNumLabels" value="2000"/>
    <property key="labeling/mergeLines" value="false"/>
    <property key="labeling/minFeatureSize" value="0"/>
    <property key="labeling/multilineAlign" value="0"/>
    <property key="labeling/multilineHeight" value="1"/>
    <property key="labeling/namedStyle" value="Bold Italic"/>
    <property key="labeling/obstacle" value="true"/>
    <property key="labeling/placeDirectionSymbol" value="0"/>
    <property key="labeling/placement" value="2"/>
    <property key="labeling/placementFlags" value="10"/>
    <property key="labeling/plussign" value="false"/>
    <property key="labeling/preserveRotation" value="true"/>
    <property key="labeling/previewBkgrdColor" value="#ffffff"/>
    <property key="labeling/priority" value="5"/>
    <property key="labeling/quadOffset" value="4"/>
    <property key="labeling/reverseDirectionSymbol" value="false"/>
    <property key="labeling/rightDirectionSymbol" value=">"/>
    <property key="labeling/scaleMax" value="10000000"/>
    <property key="labeling/scaleMin" value="1"/>
    <property key="labeling/scaleVisibility" value="false"/>
    <property key="labeling/shadowBlendMode" value="6"/>
    <property key="labeling/shadowColorB" value="0"/>
    <property key="labeling/shadowColorG" value="0"/>
    <property key="labeling/shadowColorR" value="0"/>
    <property key="labeling/shadowDraw" value="false"/>
    <property key="labeling/shadowOffsetAngle" value="135"/>
    <property key="labeling/shadowOffsetDist" value="1"/>
    <property key="labeling/shadowOffsetGlobal" value="true"/>
    <property key="labeling/shadowOffsetUnits" value="1"/>
    <property key="labeling/shadowRadius" value="1.5"/>
    <property key="labeling/shadowRadiusAlphaOnly" value="false"/>
    <property key="labeling/shadowRadiusUnits" value="1"/>
    <property key="labeling/shadowScale" value="100"/>
    <property key="labeling/shadowTransparency" value="30"/>
    <property key="labeling/shadowUnder" value="0"/>
    <property key="labeling/shapeBlendMode" value="0"/>
    <property key="labeling/shapeBorderColorA" value="255"/>
    <property key="labeling/shapeBorderColorB" value="128"/>
    <property key="labeling/shapeBorderColorG" value="128"/>
    <property key="labeling/shapeBorderColorR" value="128"/>
    <property key="labeling/shapeBorderWidth" value="0"/>
    <property key="labeling/shapeBorderWidthUnits" value="1"/>
    <property key="labeling/shapeDraw" value="false"/>
    <property key="labeling/shapeFillColorA" value="255"/>
    <property key="labeling/shapeFillColorB" value="255"/>
    <property key="labeling/shapeFillColorG" value="255"/>
    <property key="labeling/shapeFillColorR" value="255"/>
    <property key="labeling/shapeJoinStyle" value="64"/>
    <property key="labeling/shapeOffsetUnits" value="1"/>
    <property key="labeling/shapeOffsetX" value="0"/>
    <property key="labeling/shapeOffsetY" value="0"/>
    <property key="labeling/shapeRadiiUnits" value="1"/>
    <property key="labeling/shapeRadiiX" value="0"/>
    <property key="labeling/shapeRadiiY" value="0"/>
    <property key="labeling/shapeRotation" value="0"/>
    <property key="labeling/shapeRotationType" value="0"/>
    <property key="labeling/shapeSVGFile" value=""/>
    <property key="labeling/shapeSizeType" value="0"/>
    <property key="labeling/shapeSizeUnits" value="1"/>
    <property key="labeling/shapeSizeX" value="0"/>
    <property key="labeling/shapeSizeY" value="0"/>
    <property key="labeling/shapeTransparency" value="0"/>
    <property key="labeling/shapeType" value="0"/>
    <property key="labeling/textColorA" value="255"/>
    <property key="labeling/textColorB" value="0"/>
    <property key="labeling/textColorG" value="0"/>
    <property key="labeling/textColorR" value="0"/>
    <property key="labeling/textTransp" value="0"/>
    <property key="labeling/upsidedownLabels" value="0"/>
    <property key="labeling/wrapChar" value=""/>
    <property key="labeling/xOffset" value="0"/>
    <property key="labeling/xQuadOffset" value="0"/>
    <property key="labeling/yOffset" value="0"/>
    <property key="labeling/yQuadOffset" value="0"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerTransparency>0</layerTransparency>
  <displayfield>ogc_fid</displayfield>
  <label>0</label>
  <labelattributes>
    <label fieldname="" text="Label"/>
    <family fieldname="" name="Ubuntu"/>
    <size fieldname="" units="pt" value="12"/>
    <bold fieldname="" on="0"/>
    <italic fieldname="" on="0"/>
    <underline fieldname="" on="0"/>
    <strikeout fieldname="" on="0"/>
    <color fieldname="" red="0" blue="0" green="0"/>
    <x fieldname=""/>
    <y fieldname=""/>
    <offset x="0" y="0" units="pt" yfieldname="" xfieldname=""/>
    <angle fieldname="" value="0" auto="0"/>
    <alignment fieldname="" value="center"/>
    <buffercolor fieldname="" red="255" blue="255" green="255"/>
    <buffersize fieldname="" units="pt" value="1"/>
    <bufferenabled fieldname="" on=""/>
    <multilineenabled fieldname="" on=""/>
    <selectedonly on=""/>
  </labelattributes>
  <edittypes>
    <edittype labelontop="0" editable="1" type="0" name="EO.Einzelobjekt_art"/>
    <edittype labelontop="0" editable="1" type="0" name="EO.Einzelobjekt_art_txt"/>
    <edittype labelontop="0" editable="1" type="0" name="EO.Einzelobjekt_entstehung"/>
    <edittype labelontop="0" editable="1" type="0" name="EO.Einzelobjekt_gem_bfs"/>
    <edittype labelontop="0" editable="1" type="0" name="EO.Einzelobjekt_lieferdatum"/>
    <edittype labelontop="0" editable="1" type="0" name="EO.Einzelobjekt_los"/>
    <edittype labelontop="0" editable="1" type="0" name="EO.Einzelobjekt_ogc_fid"/>
    <edittype labelontop="0" editable="1" type="0" name="EO.Einzelobjekt_qualitaet"/>
    <edittype labelontop="0" editable="1" type="0" name="EO.Einzelobjekt_qualitaet_txt"/>
    <edittype labelontop="0" editable="1" type="0" name="art"/>
    <edittype labelontop="0" editable="1" type="0" name="art_txt"/>
    <edittype labelontop="0" editable="1" type="0" name="eo_tid"/>
    <edittype labelontop="0" editable="1" type="0" name="gem_bfs"/>
    <edittype labelontop="0" editable="1" type="0" name="lieferdatum"/>
    <edittype labelontop="0" editable="1" type="0" name="linienelement_von"/>
    <edittype labelontop="0" editable="1" type="0" name="los"/>
    <edittype labelontop="0" editable="1" type="0" name="ogc_fid"/>
    <edittype labelontop="0" editable="1" type="0" name="tid"/>
  </edittypes>
  <editform>.</editform>
  <editforminit></editforminit>
  <featformsuppress>0</featformsuppress>
  <annotationform>.</annotationform>
  <editorlayout>generatedlayout</editorlayout>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <attributeactions/>
</qgis>
