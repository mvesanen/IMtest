---
title: "InfraModel 4.1.0 Draft -- {{draft-version}}"
author: Inframodel 4.1.0 Working Group
geometry: "left=2cm,right=2cm,top=2cm,bottom=2cm"
xnos-warning-level: 1
xnos-number-by-section: True
---
\clearpage
{{schemafile ../schema/InfraModel.xsd}}\
# Inframodel 4.1.0, subset of LandXML 1.2


## Background
Inframodel 4.1.0,subset of LandXML 1.2 specification defines the work flow and mandatory model data exchange on infrastructure construction projects.  

LandXML is "a specialized XML data file format containing civil engineering and survey measurement data commonly used in the Land Development and Transportation Industries".
It was developed by an open community of volunteer organizations and individuals over almost a decade, until the schema version v1.2 was ratified/standardized on August 15,
2008 and published on the LandXML.org website.

Files following this specification are fully LandXML1.2 compatible, but all LandXML 1.2 files aren't compatible with this specification due the restricted subset of elements and constraints.

## Fundamental concepts and assumptions
The LandXML schema consists of specification of data types for civil engineering and survey measurement data. For practical application in civil and infrastructure design and construction scenarios common engineering concepts need to be defined, indicating use of data types for particular scenarios. The following chapters define such common concepts, which are applied at elements having specific use. Such concepts also form the basis of Model View Definitions, detailed specifications that adapt the scope and rules of the LandXML schema for targeted applications within the civil and infrastructure industry.

Each concept defines a set of elements and attributes, with constraints and parameters set for particular attributes and instance types.


## File headers {#sec:mvd-headers}  

The following items are defined in the header:

- The root element of the file (\<LandXML>)
    - Units of measurement (\<Units>)
    - Worksite information (\<Project>)
    - The feature extension used by this specification (\<FeatureDictionary>)
    - Application information (\<Application>)
    - Author information (\<Author>)

### XML File container {#sec:mvd-file}
XML files shall use UTF-8 encoding, and encoding attribute shall be set on XML header

XML-snippet:
```
<?xml version="1.0" encoding="UTF-8"?>
```


The root element (\<LandXML>) of the transfer file is used by software to check the validity of the file structure.

{{xtabulate4 LandXML}}


### Units {#sec:mvd-units}


The units used in the file are defined by the \<Units> element. Only certain metric SI system units are allowed, and those are defined under the sub-element \<Units>\<Metric>. The following table lists valid units.
Radians are used as default direction (directionUnit) and angular (angularUnit) units. These are defined counter-clockwise from the base direction. In angular definitions the base direction is east, and in direction definitions it is north.

{{xtabulate4 Metric}}

### Project {#sec:mvd-project}
Optional worksite information element.

Name is only required attribute if element is present. The description can e.g. contain the project long name or code, but is optional. The optional state attribute can be used to describe the state of the project and its content.

{{xtabulate4 Project}}

where {{xtabulate stateType}}

### Application {#sec:mvd-application}
The mandatory \<Application> element describes that software which creates the file.

{{xtabulate4 Application}}


### Authors {#sec:mvd-authors}
Information of the author of the file is recorded in the optional sub-element
\<Application>\<Author>

{{xtabulate4 Author}}

### Feature Dictionary {#sec:mvd-features}

The \<FeatureDictionary> identifies the specification source of extensions used in the file, and the point of access to their documentation.

The contents of \<Feature> elements shall follow the source specification. LandXML-files in general may contain extensions from several different sources.

In Inframodel file transfer, proper recognition and interpretation is required only for the extensions documented in this specification ( e.g. for the type coding systems used in such file). The dictionary for MDV extensions must be specified using \<FeatureDictionary> element as shown in the table below. The name is fixed to 'Inframodel' for the extensions defined in this spesification, and exactly the same name shall be set in every \<Feature> for the optional source attribute (the \<Feature> attribute code being labeled with IM_ -prefix). The \<version> shall match with the version number of this LandXML 1.2 subset's verification schema.

{{xtabulate4 FeatureDictionary}}


Proprietary extensions can be used in addition of ones specified in this specifications feature dictionary. Each source of such extension specifications shall be identified as their own \<FeatureDictionary> instance, with unique name. That name shall be set as the value of attribute source in every \<Feature> according to that dictionary. Proprietary \<Feature> instances should not have attribute code labeled with IM_ -prefix.


## Taxonomy {#sec:mvd-taxonomy}


Identification of design objects is based on taxonomy where each object belongs to object category and has feature code identifying its type in machine readable manner.
This specification ensures machine readability by harmonizing use of feature codes and categories.


### Object category {#sec:mvd-objectcategory}

Object categories are used for grouping feature codes. Different structural surfaces have their dedicated category codes. All objects in the group, for example breaklines of the structure, have their own individual feature codes. Object categories follow single code list inside one worksite. Hence, multiple design models may represent parts of the same structural layer. When as-built is stored, it is identified based on object category and can be used for tracking progress and quality of the structure in machine readable manner independently of design model. Category code may be lead from layer structure of owner's CAD data if such system doesn't exist.    

### Feature code {#sec:mvd-featurecode}

Individual feature codes are set for:

- Data point groups, in the \<DataPoints> element
- Breaklines in the \<BreakLine> element
- Surfaces, in the \<Surfaces> or \<Surface> element
- Alignments, in the \<Alignments> or \<Alignment> element
- Points, in the \<CgPoints> or \<CgPoint> element
- String line layers, in the "IM_StringlineLayer(s)" \<Feature> extension element
- Other infrastructures in appropriate elements, such as \<PlanFeature>, \<Pipenetwork>, \<Pipe> or \<Struct>

Object categories and feature codes are set in the child elements, or in the parent element whose children inherit the values. However, if value is set on both levels, child value overrides parent value.  

Object categories and feature codes are set using the IM_Taxonomy \<Feature> extension see {{refsec mvd-typecodingsystems}}


## Surface mesh {#sec:mvd-basedata}

Surface mesh is a triangulated representation of the topography, which may also contain the original source data used for the triangulation process (as datapoints and boundaries). Breaklines are not typically used to form surfaces, but if transferred under \<Surface> as source data, they shall coincide with the triangulation defining the surface, i.e. each pair of consecutive breakline points given in 3D coordinates, shall match the coordinates of two vertices of a triangle.

Surface meshes are used for soil topmost surface and ground layer models (top surface of each layer) as described in this section. They are also used for structural models of roads, streets, railways, waterways and areal structures, as described in sections 4 - 8.

Surfaces and source data is described as surface groups \<Surfaces>, which are made of individual \<Surface>-elements. The name of every surface group and the name of each surface within the file are unique.

{{xtabulate Surfaces}}

{{xtabulate5 Surface}}

#### Current and planned surfaces {#sec:mvd-currentandplannedsurfaces}
An existing surface is defined by setting the state of the \<Surfaces> or \<Surface> element to "existing". If it is proposed the state is set to "proposed". If all the surfaces within a surface group have the same state, it is possible to set the state on a higher level in the surface group \<Surfaces>. The state for an individual surface is set if the constituent triangle meshes, data points and breaklines are is the same state.

#### Taxonomy of surface meshes {#sec:mvd-typecoding}

Object category and feature code shall be set for following elements:

- in the element \<DataPoints> for source data points
- in the element \<BreakLine> for breaklines
- in the element \<Surface> for single surface
- in the element \<Surfaces> for surfaces group

### Source data {#sec:mvd-sourcedata}

The source data is described by the element \<SourceData>. This element has no attributes.
Source data consists of:

- Source data points \<DataPoints> and
- Breaklines \<BreakLines>
- Boundaries \<Boundary>

![]({{figure IM_Drawings_F-01.jpg}})

#### Data points {#sec:mvd-datapoints}
Source data points are described by the element <DataPoints>, sorting every point group into individual elements.

{{xtabulate5 DataPoints}}


The point group is classified by IM_Taxonomy feature. The individual data points in the \<DataPoints> point group are presented as a 3D coordinate list in the \<PntList3D> element, values separated by spaces
\<PntList3D>northing1 easting1 elevation1 northing2 easting2 elevation2...\</PntList3D>


#### Breaklines {#sec:mvd-breaklines}
In the breakline group \<BreakLines>, where each \<BreakLine> is presented in its own element. The breakline group has no attributes. In \<BreakLine> the breakline type brkType defines the use in software.

{{xtabulate5 Breakline}}

Attributes of an individual \<BreakLine>:

Breaklines are classified by IM_Taxonomy and they can be given individual names. The constituent points of a \<BreakLine> are described as a 3D coordinate list in the \<PntList3D> element, values separated by spaces

\<PntList3D>northing1 easting1 elevation1 northing2 easting2 elevation2..\</PntList3D>



#### Boundaries {#sec:mvd-boundaries}
Additionally, it is also possible to define boundaries of the mesh source data in the optional boundary group \<Boundaries>, where each \<Boundary> is presented in its own element. The boundary group has no attributes. In \<Boundary> the mandatory attributes boundary type bndType and edge trim edgeTrim define the use in software. Additionally, optional attributes for area, name, description and state can be set.

{{xtabulate5 Boundary}}

{{xtabulate surfBndType}}


The points of a \<Boundary> are described as a 2D coordinate list in the \<PntList2D> element, values separated by spaces

\<PntList2D>northing1 easting1 northing2 easting2 ...\</PntList2D>

### Triangulated mesh surface {#sec:mvd-triangulatedmeshsurface}

Surface geometry is described as triangulated meshes. Each surface is defined under the \<Definition> in terms of boundaries, exterior features and holes. A triangular mesh is defined in two steps; first by defining the vertices of the triangular faces as surface points, and then each individual face by three vertices. The surface points used as vertices are assigned unique identifiers id within the same surface definition (\<Surface>\<Definition>) element. The face definitions are done by referring to the id numbers of the vertex points.
Additionally, the surface is given an type code according to the declared IM_Taxonomy.

![]({{figure IM_Drawings_F-02.jpg}})

It is mandatory to set surfType to "TIN" when describing a triangular mesh. The precision of the mesh model depends on the available software and data. It is possible to optionally describe a 2D surface area area2DSurf, 3D surface area area3DSurf and the maximum elevation elevMax and minimum elevation elevMin.

{{xtabulate4 Definition}}


#### Vertices {#sec:mvd-vertices}

The vertex point group \<Pnts> contains a listing of individual vertices \<P>, which are each assigned an individual id number id. These numbers are referenced in the triangulation.

{{xtabulate Pnts}}

{{xtabulate5 P}}


where {{xtabulate Point}}


The vertices of a surface definition, minimum three of them, are given as \<P> elements, where the 3D coordinates are separated by spaces.

\<P id="1">northing1 easting1 elevation1\</P>

\<P id="2">northing2 easting2 elevation2\</P>

\<P id="3">northing3 easting3 elevation3\</P>

#### Faces {#sec:mvd-faces}
The triangulation is defined in the \<Faces> collection. It consists of consecutive list of faces \<F>. The order of the faces implicitly defines the index number of each triangle (1,2,...). Each face is defined by referencing three vertex id numbers. Triangle normal direction is defined with the winding order of face vertices. Clockwise winding order defines a front facing triangle as shown in the figure below.

{{xtabulate4 Faces}}

{{xtabulate4 F}}

![]({{figure IM_Drawings_F-03.jpg}})



### Soil topmost surface {#sec:mvd-terrainmodel}
The digital elevation model in \<Surfaces> contains the description of the existing soil surface as one or more \<Surface>. It consists of the vertices of the component faces \<Pnts> and the faces \<Faces> as explained in {{refsec mvd-basedata}}. In files following this specification it is also possible to assign source data points and breaklines to the surface. An IM\_Taxonomy type coding provides surface classification.


### Geotechnical model {#sec:mvd-groundlayermodel}
The geotechnical model (\<Surfaces>) contains a description of all the surfaces (\<Surface>) between ground layers. Individual layer surfaces are constructed as explained section 2.3.  An IM\_Taxonomy type coding provides surface classifications.


## Route planning across domains {#sec:mvd-Routeplanning}

Routes encompass highways, local roads and private roads, waterways and railways. Each route has one continuous stationing reference alignment and a vertical alignment. A route plan consists of parametric route alignments, and combination of their line models and/or triangulated meshes.
This documentation discusses individually different route types: 1) roads and streets 2) railways 3) waterways which are described in following chapters.

An alignment group \<Alignments> consists of several alignments \<Alignment>. Alignments can be described in two ways:

- Geometric alignment
- Line string


Geometric alignments describe parameters of the horizontal and vertical elements of an alignment. A line string is a description where consecutive points are connected by line segments. Geometric alignments are typically used to describe the reference alignment of a route as well as other important geometric descriptions such as kerb. Other route breaklines are usually described as alignment line strings.

![]({{figure IM_Drawings_F-04.jpg}})


##### Route description {#sec:mvd-routedescription}
Route description is driven by stationing reference alignment. All geometry lines of the same route are given in the same alignment collection \<Alignments>, each as separate alignment \<Alignment>.

### Composing alignments {#sec:mvd-composingalignments}

{{xtabulate4 Alignments}}



The alignments within a file do not have to be presented in any particular order. It is, however, advisable to first describe geometric alignments and then line strings. It is recommended that descriptions of alignments are given in an intuitive fashion. If the state is set for the entire alignment group \<Alignments> the \<Alignment> elements will inherit the state attribute from the parent element.

{{xtabulate4 Alignment}}


#### Taxonomy of alignments {#sec:mvd-alignmenttypecoding}
Object category and feature code shall be set either for each \<Alignments> parent element, whose children inherit the values, or for each \<Alignment> element which value overrides the parent value in case where both are defined. The object category and feature code is set by the IM_Taxonomy \<Feature> extension. More details: {{refsec mvd-typecodingsystems}}


### Alignment geometry {#sec:mvd-alignmentgeometry}

The geometric alignment contains the horizontal and vertical alignment information. The horizontal alignment information is described in the \<CoordGeom> and the corresponding vertical geometry in the element  \<Profile>\<ProfAlign> when available. For the connection between horizontal and vertical geometry it is mandatory that the geometric description is continuous. Continuous means that all elements are connected in a chain and their tangents meet. The horizontal geometry is described using a 2D or 3D coordinate representation. In case of 2D horizontal geometry, the final elevation values along the alignment can only be produced only after vertical geometry is applied. The illustration below shows the horizontal and vertical geometry definition and their connection principle. The optional staStart attribute in \<Line>, \<Curve>, \<Spiral> and \<Profile> shall not be used for calculating horizontal or vertical coordinates, but it could be used for precise stationing equations.

![]({{figure IM_Drawings_F-05.jpg}})

#### Horizontal geometry {#sec:mvd-horizontalalignments}

Horizontal alignment geometry is in the \<CoordGeom> element

{{xtabulate CoordGeom}}


The elements of horizontal alignments:

- \<Line>
- \<Curve>
- \<Spiral>

The horizontal alignment is a listing of consecutive elements, starting at the staStart of the parent \<Alignment>.

![]({{figure IM_Drawings_F-06.jpg}})

#### Line <a name="3311line"></a>
A \<Line> is defined by \<Start> and \<End> 2D or 3D coordinates.

{{xtabulate Line}}


The format for the \<Start> and \<End> coordinates of a \<Line>, the 2D or 3D coordinates are separated by spaces.

\<Start>northing1 easting1\</Start>

\<Start>northing1 easting1 altitude1\</Start>

\<End>northing2 easting2\</End>

\<End>northing2 easting2 altitude2\</End>

#### Curve {#sec:mvd-curve}
A circular arc \<Curve> is defined by \<Start> \<Center> and \<End> 2D or 3D coordinates.
The distance from the \<Start> to the \<Center> provides the radius value of the curve if radius attribute is not present.

{{xtabulate Curve}}

{{xtabulate rotDir}}


The  \<Start>, \<Center> and \<End> of a \<Curve>, the 2D or 3D coordinates are separated by spaces.

\<Start>northing1 easting1\</Start>

\<Start>northing1 easting1 altitude1\</Start>

\<Center>northing2 easting2\</Center>

\<Center>northing1 easting1 altitude2\</Center>

\<End>northing3 easting3\</End>

\<End>northing1 easting1 altitude3\</End>

#### Transition curve {#sec:mvd-Transitioncurve}

A \<Spiral> is defined by \<Start>, point of intersection of the end tangents \<PI> and \<End>Coordinates. Allowed transition curve type are:

- an Euler spiral "clothoid"
- bi-quadratic parabola "biquadraticParabola"
- third-degree spiral "cubic"

{{xtabulate Spiral}}

{{xtabulate rotDir}}

{{xtabulate spiralType}}


The \<Start>, point on intersection of start and end tangents \<PI> and \<End> are defined as 2D coordinates separated by spaces.

\<Start>northing1 easting1\</Start>

\<PI>northing2 easting2\</PI>

\<End>northing3 easting3\</End>

#### Vertical geometry {#sec:mvd-verticalalignments}

The vertical geometry is described in the \<Profile>\<ProfAlign> element under the same \<Alignment> with the horizontal geometry definition. Each horizontal geometry can have only one (or 0) vertical geometry. The elements of the vertical geometry are:

- Point of Vertical Intersection \<PVI>
- Vertical circular arc \<CircCurve>
- Parabolic vertical curve \<ParaCurve>

![]({{figure IM_Drawings_F-07.jpg}})


{{xtabulate Profile}}


#### Point of vertical intersection {#sec:mvd-pointofverticalintersection}

The first and last element of the vertical profile is always a Point of Vertical Intersection\<PVI>.

A Point of Vertical Intersection \<PVI> marks the ends of the line segments of a vertical geometry. A Point of Vertical Intersection is described by a station and an elevation. These are separated by a space.

{{xtabulate5 PVI}}

#### Vertical curve {#sec:mvd-verticalcurve}

Vertical circular arcs may be combined into S-curves or compound curves.

The location of the <CircCurve> is defined by the station and elevation, separated by spaces.

{{xtabulate5 CircCurve}}



### Parabolic curve {#sec:mvd-paracurve}
The Parabolic curve \<ParaCurve> is defined by attribute length and by space separated station and elevation values for vertical intersection point.

{{xtabulate5 ParaCurve}}


### Line strings {#sec:mvd-linestrings}

Line strings are defined in \<CoordGeom>\<IrregularLine> element as 2D or 3D points.  In case of 2D points a vertical \<Profile> element may be applied for 3D representation.


#### Line string {#sec:mvd-linestring}
A line string shall have sub-elements to define its \<Start> and \<End> coordinates. Intermediate 2D or 3D points shall be defined either as \<PntList2D> or \<PntList3D>.

The \<Start> and \<End> points of an \<IrregularLine> are individual coordinates are separated by spaces.

The 2D point list \<PntList2D> consists of 2D coordinates of intermediate points and start and end points, separated by spaces.

\<PntList2D>northing1 easting1 northing2 easting2 northing3 easting3...\</PntList2D>


The 3D point list \<PntList3D> consists of 3D coordinates of intermediate points and start and end points, separated by spaces.

\<PntList3D>northing1 easting1 elevation1 northing2 easting2 elevation2 northing3 easting3 elevation3...\</PntList3D>

{{xtabulate5 IrregularLine}}


### String line representation of surface {#sec:mvd-stringlinemodel}

An alignment group \<Alignments> is a collection of geometric alignments and/or line strings. The string line model used in this documentation is based on the Leica RoadRunner \<RR\_StringLineLayers> \/ \<RR\_StringlineLayer> feature extensions, but is renamed as \<IM\_StringLineLayers> \/ \<IM\_StringlineLayer>.

![]({{figure IM_Drawings_F-08.jpg}})


The string line model of a \<Alignments> alignment group is defined by the IM\_StringlineLayers \<Feature> extension. The string line model is a surface generated from set of alignments listed in IM\_StringlineLayer \<Feature> child element. Unique names of alignments are used as identifiers. Each surface of the string line model \<IM\_StringlineLayer> shall have a unique name.

The procedure for constructing a new surface in the string line model in the "IM\_StringlineLayers" extension:

1. The surface <IM\_StringlineLayer> is assigned a unique name.
2. The line string alignments are listed from left to right towards increasing stationing. The list is separated by commas.
3. The centerline property value is set. centerline has to be one of the alignments listed.
4. The categoryCode shall be set via IM\_Taxonomy \<feature> extension.

A line string may belong to multiple surfaces.

The detailed description of the stringline model can be found in {{refsec mvd-stringlinemodel}}

### Cross-section model {#sec:mvd-crosssections}
The cross-sections along an alignment may be set in \<Alignment>\<CrossSects>\<CrossSect> as a geometric representation. Cross-sections may provide parametric information at given station intervals (e.g. each 20 meters or at transitions). Additional domain specific parameters are set in the IM_CrossSect extension along with the cross-section elements, as described in following chapters 6, 7 and 8.

The cross-section parameters describe the situation at a given station. The following elaborates on the process of description: the cross-section parameters are presented at a station where a value begins or stops changing.

{{xtabulate CrossSects}}

{{xtabulate CrossSect}}

The planned cross-sections may be represented by design cross-section surfaces set in \<DesignCrossSectSurf> where each cross-section point is given by \<CrossSectPnt> as a space separated value pairs "Offset Elevation". Offsets are measured horizontally in linear units from the center line (positive values to the right).

![]({{figure IM_Drawings_F-09.jpg}})

{{xtabulate DesignCrossSectSurf}}

{{xtabulate CrossSectPnt}}

{{xtabulate dataFormatType}}


### Cross-section domain specific parameters {#sec:mvd-crosssectionparameters}

Cross-section parameters refer to parametric information complementing the model represented as surface or stringline models. These include design parameters such as the widths and superelevations of roads.
The relevant cross-section parameters for each route type are described in further detail in the corresponding section of each route type.



### Structural model {#sec:mvd-structuralmodel}

Structural model of a route can be represented as a combination of stringline layers, surface meshes and cross-sections. Stringline layers are most efficient for data exchange of machine readable structural model. However stringline layers can be problematic on eg. intersection, roundabouts and extremely tight corners. In these cases, surface mesh can provide a more accurate structural model. Cross-sections shall not be used to generate structural model. However cross-sections can provide useful design parameters for eg. railway track placement, and cross-sections can be used to validate geometry of structural model.



## Roads and streets {#sec:mvd-roadsandstreets}

A road or street alignment is defined according to the process defined in chapter {{refsec mvd-Routeplanning}}. A single design file may contain several route plans from several domains, i.e. the same file may contain e.g. road, street, and railway plans.

Street designs often interface with water supply and sewerage systems that may be described in the same or several design files.


A structural model of road or street design may contain:

- individual alignments and their purpose, defined by type coding (geometric alignments and line strings)
- stringline models (line string alignments)
- surface meshes (TIN surface)
- cross-section models


The superelevation of the road may be described alongside the cross-section parameters. Cross-section parameters are described at the transition points, when the transition of the value of a parameter begins or ends. Superelevation encompasses the cross slope of the roadway and in case of a street also the sidewalk.


### Geometry {#sec:mvd-geometry}
The central alignments such as the centerline and left and right edges of a road or the centerline and edges of a sidewalk for a street are typically described as geometric alignments while the rest are described in terms of line strings.

### String line model {#sec:mvd-roadstringlinemodel}

The detailed description of the stringline model can be found in {{refsec mvd-stringlinemodel}}

### Cross-sections {#sec:mvd-roadcrosssectionsandslopes}
The detailed description of the cross-section model can be found in {{refsec mvd-crosssections}}

#### Cross-section parameters {#sec:mvd-roadcrosssectparameters}
The cross-section parameters are set for the stationing reference alignment cross-sections \<Alignment>.\<CrossSects>.\<CrossSect> in the  optional IM_CrossSect \<Feature> extension . The first cross-section of the alignment is defined by describing all parameters of the cross-section. The parameters of the following cross-sections are only described if a value begins or stops changing.

The following paramaters may be defined in the IM_CrossSect \<Feature> extension for each individual cross-section:

- Pavement class
- Pavement thickness
- Load capacity (kN/m2)

More details about IM_CrossSect \<Feature> extension can be found {{refsec mvd-crossectionparametersextension}}

#### Transitions in superelevation {#sec:mvd-roadslopetransitions}

The superelevation is indicating the transition points, when a transition in the superelevation either begins or end. The cross-slopes are defined along with the cross-section parameters. The following picture illustrates the process in a road design environment.

![Transitions in superelevation]({{figure IM_Drawings_F-10.jpg}}){{figst superelevation}}


### Structural model {#sec:mvd-roadterrainandstructuralmodel}
The process of constructing structural model of a road or street is described in detail in the {{refsec mvd-structuralmodel}}

The example illustrations below demonstrate the composition of structural models (as Surface meshes) in road and street design.

![]({{figure IM_Drawings_F-11.jpg}})

![]({{figure IM_Drawings_F-12.jpg}})



### Road plan features {#sec:mvd-roadplanfeatures}
The road planimetric features such as fences, guard rails, light pole or signage footings that are assigned to a particular road or street are described under \<Roadways> element. A roadways collection \<Roadways> may consist of several roadway \<Roadway> elements. Each roadway has a reference to its stationing reference lines \<Alignment>.name, and it can hold a number of \<PlanFeature>.

{{xtabulate Roadways}}

{{xtabulate Roadway}}

More details about plan features can be found from {{refsec mvd-planimetricfeatures}}


## Railways {#sec:mvd-railways}


The methods used to describe a route are described in detail in the {{refsec mvd-Routeplanning}}. A railway plan typically consists of one continuous track for railway stationing and other tracks. The centerlines and the bottoms of the rails of each track are typically described as geometric alignments. The transition points for cant and design speeds may also be described. This is done in conjunction with the stationing of the centerline of the railway stationing track.

### Geometry {#sec:mvd-railgeometry}

One or more \<Alignment> elements are used for describing a railway geometry. Only one of those \<Alignment> elements can be the centerline of the reference track for railway stationing.

The geometric alignments are defined as described in {{refsec mvd-alignmentgeometry}}. The distance-posting reference track and additional track center lines shall have their own feature codes. Other lines than centerlines and the bottoms of the rails are typically described as line strings. The object category and feature code of individual alignment determine their purpose.

### String line model {#sec:mvd-railstringlinemodel}

The detailed description of the stringline model can be found in {{refsec mvd-stringlinemodel}}

### Railway stationing {#sec:mvd-kmposting}

Railway stationing may be nonlinear. Nonlinear definition is done by adding two or more \<StaEquation> elements under the distance-posting reference \<Alignment>. In case of linear stationing, the \<Alignment> elements staStart attribute defines the station offset.

An individual nonlinear station equation is defined by the previous station equation. Hence the \<staAhead> attribute is always set to 0.000000 according to this specification. Individual stations along the tracks of an alignment are presented in conjunction with the \<Alignment> as \<StaEquation> element list. For every track the distance between stations is defined by the distance from a particular station to the previous station using the \<staBack> attribute. The name of the station is defined by the \<desc> attribute.

The actual length of a track is described by a continuous internal stationing, defined by the \<staInternal> attribute.

{{xtabulate StaEquation}}

{{xtabulate stationIncrementDirectionType}}

### Cross-sections and tracks {#sec:mvd-railcrosssectionsandtracks}
The detailed description of the cross-section model can be found in {{refsec mvd-crosssections}}

#### Cross-sections {#sec:mvd-railcrosssections}
For individual cross-sections, the cross-section parameters are set in the IM_CrossSect \<Feature> extension under \<Alignment>\<CrossSects>\<CrossSect>. Transitions are defined by describing the points where parameters change and where they have reached their final value after the transition. The parameters are valid from the station they are set to onwards. Triple or more track railways are composed of double- and single-track standard cross-sections.

The following paramaters may be defined in the IM_CrossSect \<Feature> extension for each individual cross-section:

- the number of tracks
- the distance between track centerlines
- the total thickness of track bed layers
- track bed or cut width

More details about IM_CrossSect <Feature> extension can be found {{refsec mvd-crossectionparametersextension}}

#### Tracks {#sec:mvd-tracks}
The transitions in cant and design speed for the Stationing reference track and track centerlines are described with the \<Alignment>\<Cant> sub-element. The track information \<Cant> defines a name, the track gauge and the track rotation point rotationPoint.

{{xtabulate Cant}}



The following transitions are described in the track information sub-element:
 \<CantStation> is used when the cant and possibly design speed change

{{xtabulate CantStation}}

{{xtabulate rotDir}}

{{xtabulate stationIncrementDirectionType}}

 \<SpeedStation> is used when only design speed changes

 {{xtabulate SpeedStation}}

![]({{figure IM_Drawings_F-13.jpg}})





### Structural model {#sec:mvd-terrainandstructuralmodel}
The process of constructing structural model of a railway is described in detail in the {{refsec mvd-structuralmodel}}


### Railway plan features {#sec:mvd-railplanfeatures}
The railway planimetric features such as switches, crossings, fences, guard rails, light pole or signage footings that are assigned to a particular railway are described under roadways. See {{refsec mvd-roadplanfeatures}} for details.


## Waterways {#sec:mvd-waterways}

The methods used to describe a waterway route are described in detail in the {{refsec mvd-Routeplanning}}.
An waterway design contains at least one alignment group \<Alignments> composed of alignments \<Alignment> and should include waterway structural model.

### Geometry {#sec:mvd-waterwaygeometry}
Waterways \<Alignments> shall have a at least one continuous stationing reference alignment. This alignment and other central alignments are typically presented as geometric alignments. In waterway designs, the stationing reference line and the left and right edge alignments are also usually described as geometric alignments. Other alignments are typically described in terms of line strings.
The elevation of the stationing reference alignment may be set to the average lowest height of the sailing season in inland bodies of water.


### Cross-section parameters {#sec:mvd-waterwaycrosssectionparameters}
The detailed description of the cross-section model can be found in {{refsec mvd-crosssections}}


The cross-section parameters are set for the stationing reference alignment cross-sections <Alignment>.<CrossSects>.<CrossSect> in the IM_CrossSect <Feature> extension . The first cross-section of the alignment is defined by describing all parameters of the cross-section. The parameters of the following cross-sections are only described if a value begins or stops changing.

Following parameters may be set via IM_CrossSect <Feature>
- minimum depth
- minimum width
- dimensioning waterLevel

More details about IM_CrossSect <Feature> extension can be found {{refsec mvd-crossectionparametersextension}}


### String line model {#sec:mvd-waterwaystringlinemodel}

The detailed description of the stringline model can be found in {{refsec mvd-stringlinemodel}}


### Structural model {#sec:mvd-waterwayterrainandstructuralmodel}

The process of constructing a structural model of a railway is described in detail in the {{refsec mvd-structuralmodel}}.


### Waterway plan features {#sec:mvd-waterwayplanfeatures}
The waterway planimetric features such as navigation buoys that are assigned to a particular waterway are described under roadways.
See {{refsec mvd-roadplanfeatures}} for details.


## Areal structures {#sec:mvd-arealstructures}

Areal structures encompass descriptions of surfaces that complement routes in complicated parts of design. Such surfaces are e.g. intersection areas, roundabouts, landscaping, noise barriers and complex geostructures. Area structures are described as mesh surfaces \<Surface> as described in {{refsec mvd-triangulatedmeshsurface}}. Area structures may be described in the same file as the route they are built in conjunction with, e.g. a noise barrier is in the same file as the railway it is built for. Object category set for area structure links the design for corresponding course structural model.


## Pipeworks {#sec:mvd-watersupplyandsewerage}

Pipework designs may be described in the same LandXML file as the rest of the design content.
The pipe networks in the LandXML1.2 are topological. The model provides means to transport e.g drainage, sewerage and water supply network designs to field equipment. The following network types are implemented in the LandXML1.2d: storm drain, sewer, water pipe and 'other'. 'Other' types may be defined by using \<Feature> "IM_PipeNetworkType" extension for other network types.

Structures, such as different kind of eg. drain wells or joints are nodes. Pipes are situated between two nodes. The end of the pipe eg. culvert are modelled as virtual structures of two types, inlet and outlet.

The network topology is presented in the parent element \<PipeNetworks> whose child elements are individual \<PipeNetwork> elements. A \<PipeNetwork> consists of structures and pipes.

Structures \<Structs>

- Types: round and rectangular wells, virtual structures, equipment and pipe joints, extensions and inflexions.
- Are given an exact location
- The pipe inlet is an \<Invert>

Pipes \<Pipes>

- Types: Circular pipe, elliptic pipe, egg-shaped pipe, rectangular pipe and channel
- Pipes have reference by name to start and end structures
- The definition length is given as the distance between the centers of the terminal structures in the elevation of the inverts.
- The exact length is the arithmetic distance between the start and end coordinates of the pipe.


![]({{figure IM_Drawings_F-14.jpg}})

The pipe network is typically described in its entirety. LandXML does not allow you to delimit the network without termination of topology. That is typically done by defining delimiting inverts and pipes for separate LandXML file containing new entirety of pipework design.

### Pipe networks {#sec:mvd-pipenetworks}
A file may contain multiple pipe network groups \<PipeNetworks>.

The pipe network groups are assigned unique names. Network group contains only network in a specific state. Other states of network (eg. existing) shall be defined as a separate network.

{{xtabulate PipeNetworks}}


### Pipe network {#sec:mvd-pipenetwork}

Individual networks are defined by \<PipeNetwork> elements organized under their parent element \<PipeNetworks>, the network group. The number of networks in one network group is unlimited. The \<PipeNetwork> defines a topological model of pipe network.


{{xtabulate PipeNetwork}}


#### Pipe network type extensions <a name="831pipenetworktypeextensions"></a>

When the pipe network type is other than one of those covered by the pipeNetType attribute of the \<PipeNetwork> element, the optional "IM_PipeNetworkType" \<Feature> extension shall be used (with the pipeNetType attribute set to "other").

TODO:Link to IM_PipeNetworkType

### Structures <a name="85structures"></a>

The different structures in the \<PipeNetwork> compose the structure group \<Structs>, that has no attributes.

LandXML standard structure types:

- Circular structures
- Rectangular structures
- Pipe inlets
- Pipe outlet
- Pipe joints, extensions or points of intersection
- Equipment

Individual structs are defined under \<Struct> element.

{{xtabulate Struct}}


#### Circular structures {#sec:mvd-circularstructure}
Inspection wells of French drains are an example of a circular structure. Circular structures are defined using the structure element \<Struct> and its child elements.
The figure below illustrates the representation of a drain well, including a sump. The sump is defined in the extension "IM_Struct" \<Feature> extension by defining the sump height and volume.

![]({{figure IM_Drawings_F-15.jpg}})

{{xtabulate CircStruct}}

The well cone and sump are described in further detail in the extension "IM_Struct" \<Feature> extension. More details can be found from {{refsec mvd-structuredetails}}.

#### Rectangular structures {#sec:mvd-rectangularstructures}
The illustration demonstrates the method of description of a rectangular well, including a sump as an example. The sump is defined by its depth and/or volume.

![]({{figure IM_Drawings_F-16.jpg}})

{{xtabulate RectStruct}}


#### Pipe inlets and outlets {#sec:mvd-pipeinletsandoutlets}
Pipe inlets and outlets are the end of the pipe network pipes. The following illustration demonstrates the method of description. The virtual structures of the pipe ends are defined using the structure attribute \<Struct> and its child elements.

The illustration below demonstrates how pipe inlets and outlets are described. The example demonstrates an outlet.

![]({{figure IM_Drawings_F-17.jpg}})

Inlets \<InletStruct> and outlets \<OutletStruct> have no attributes.

#### Pipe connections {#sec:mvd-pipeconnection}
Pipe connections, joints and points of intersection are defined by the \<Connection> elements. The illustration below demonstrates the mode of description, which contains the attributes of the structure \<Struct> and its child elements

The illustration demonstrates the description method of a point of intersection.
When using the element to delimit a pipe network, the terminal drainage well is connected to a pipe that terminates in a \<Connection> element. It is thus possible to also describe the connections of the outermost wells in the plan network.

![]({{figure IM_Drawings_F-18.jpg}})

Connections, joints or points of intersection are defined using the \<Connection> element that has no attributes.

It is optional to present additional information with "IM_Struct" \<Feature> extension.

#### Equipment {#sec:mvd-equipment}
Equipment is defined using the \<Connection> element. The illustration below describes the mode of description of a structure \<Struct> and its child elements

The illustration demonstrates the mode of description of a valve:

![]({{figure IM_Drawings_F-19.jpg}})

A piece of equipment is defined using the element \<Connection>, that has no attributes.


It is optional to present additional information with "IM_Struct" \<Feature> extension. It is possible to define more detailed type information of a piece of equipment between two pipes, e.g. a valve using the attributes equipmentCategory and equipmentCode.


##### Inverts {#sec:mvd-inverts}
The adjoining inlet and outlet inverts are described using the element \<Invert>. The required attributes of invert are: the elevation \<elev> as the crown level for pressure pipes and the invert level for others, the flow direction \<flowDir> and the pipe reference \<refPipe>.

{{xtabulate Invert}}


### Pipes {#sec:mvd-pipes}
 The pipes that compose the \<PipeNetwork> are described as a structure collection \<Pipes> that has no attributes. A \<Pipe> is defined between two structure nodes \<Struct> by referring to them by name in the start- and end-attributes.

NOTE: In the special case of "network" where there is only one single pipe (such as a culvert with no specified connection at either end), the referenced start and end structure shall be \<InletStruct> and \<OutletStruct>, respectively.

Available pipe types in the LandXML standard:

- Circular pipe
- Egg-shaped pipe
- Elliptic pipe
- Rectangular pipe
- Channel


{{xtabulate Pipe}}

Following details shall be provided for pipes in "IM_Pipe" \<Feature> extension:
-  The start and end coordinates of a pipe are defined by three parameters:
    - Elevation type elevType
    - Start coordinate pipeStart
    - End coordinate pipeEnd.
Following details may be provided for pipes in "IM_Pipe" \<Feature> extension:    
    - Type of the joint for pipe jointType
    - Pressure classification of a pipe pressureClass


Elevation type shall be given as one of the enumerated elevTypes shown below.

![]({{figure IM_Drawings_F-20.jpg}})

***A="crown level", B="center level", C="invert level", D="bottom level"***

The following illustration describes the example of a typical pipe.

![]({{figure IM_Drawings_F-21.jpg}})

***A,C=structs (ie. wells) , B=pipe joint 5,6=Attachment points (elevType enum)***


More details can be found from {{refsec mvd-pipedetails}}

#### Circular pipes {#sec:mvd-circularpipes}

The definition employs the element \<Pipe> and its child element \<CircPipe>.

{{xtabulate CircPipe}}

#### Egg pipes {#sec:mvd-eggpipes}

The definition employs the element \<Pipe> and its child element \<EggPipe>.

{{xtabulate EggPipe}}

#### Elliptic pipes {#sec:mvd-ellipticpipe}

The definition employs the element \<Pipe> and its child element \<ElliPipe>.


{{xtabulate ElliPipe}}

#### Rectangular pipes {#sec:mvd-rectangularpipe}

The definition employs the element \<Pipe> and its child element \<RectPipe>.

{{xtabulate RectPipe}}

#### Channels {#sec:mvd-channels}

The definition employs the element \<Pipe> and its child element \<Channel>.

{{xtabulate Channel}}


## Planimetric features {#sec:mvd-planimetricfeatures}
Planimetric features, such as cables, light poles or signage footings, railings and fences, or any other objects not otherwise defined by this LandXML 1.2 subset are described using \<PlanFeature> element. These features often interface with routes (road, street, rail or waterway). In such cases they should be described under \<Roadways> collection.

The planimetric features not directly assigned to any particular route (road, street, rail or waterway) are grouped in one or more planimetric feature collections \<PlanFeatures> consisting of several \<PlanFeature> elements. Each \<PlanFeatures> collection shall have a unique name.

{{xtabulate PlanFeatures}}


The individual plan features are each described under \<PlanFeature>

{{xtabulate5 PlanFeature}}


\<PlanFeature> geometry is described in \<CoordGeom> using line strings for linear features, e.g. cables, railings and fences. In case of area, structure boundaries are used. Also circular or spiral curve arcs may be used. For point features, such as footings, location is given in \<Location> element as a two or three dimensional point:

\<Location>northing easting (elevation)\<Location>

Object category and feature code shall be set either for each \<PlanFeatures> parent element, whose children inherit the values, or for each \<PlanFeature> element which value overrides the parent value in case where both are defined. The object category and feature code is set by the IM_Taxonomy \<Feature> extension.


### Spatial allocation and avoidance {#sec:mvd-cables}

Spatial allocation is a boundary connected to planimetric object geometry eg. a space reservation for electric cable installation. Such \<Planfeatures> or \<Planfeature> elements shall have their state attribute set as "proposed". Spatial allocation may be 2D or 3D depending of planimetric source data.

Spatial avoidance is a boundary connected to planimetric object geometry eg. a safety distance for existing electric underground cable or overhead power line. Such \<Planfeatures> or \<Planfeature> elements shall have their state attribute set as "existing". Spatial avoidance may be 2D or 3D depending of planimetric source data. Source geometry uncertainty should be taken in account when defining avoidance to existing objects.

Spatial allocation and avoidance parameters are defined with IM_Spatial \<Feature> extension by setting the Allocation and Avoidance properties.

Allocation and avoidance may also appear in the same IM_Spatial \<Feature> extension. Eg. designed cable needs to be avoided after installation.

![]({{figure IM_Drawings_F-22.jpg}})

More details can be found from {{refsec mvd-spatialallocandavoidance}}



## Other point-like objects{#sec:mvd-surveycontrolandotherpoints}
Preferred way for specifying point-like objects eg. footings that belong to the design of a route are defined on chapter [10 Planimetric features](#planimetricfeatures).

This chapter defines a secondary method that may be used for the same purpose but without a link to \<RoadWay> collection element.


{{xtabulate CgPoints}}

{{xtabulate CgPoint}}


Object category and feature code of the points shall be defined with IM_Taxonomy \<Feature> extension placed under <CgPoints> collection or under the individual <CgPoint> element. In the case of \<CgPoint>, the setting overrides the parent value.

## LandXML \<Feature> extension definitions {#sec:mvd-featureextensions}


Transfer files compliant with this LandXML 1.2 subset fully conform to the LandXML v1.2 schema, but some extensions have been made using the landxml \<Feature>-mechanism.
This section lists these extensions,specifying the \<Feature> elements in the file with \<Feature> elements attribute "code" being labeled with ''IM_' -prefix.

NB: In addition to these extensions, this subset of LandXML 1.2 specifies many restrictions on the use of LandXML elements and their attributes.

{{xtabulate Feature}}

### Taxonomy \<Feature> extension {#sec:mvd-typecodingsystems}
Taxonomy extension provides identification of geometric elements, such as points, lines,surfaces,plan features, pipes and structures.  Individual category and feature codes are set under parent elements or its child elements by using IM_Taxonomy \<Feature> extension. Child elements inherit parent taxonomy and may override the parent values.

{{xtabulate2 IM_Taxonomy_categoryCode--ltProperty--gt}}

{{xtabulate2 IM_Taxonomy_featureCode--ltProperty--gt}}

{{xtabulate5 IM_Taxonomy--ltFeature--gt}}


### String line model \<Feature> extensions  {#sec:mvd-stringlinemodelextension}

The string line model is composed of  alignments. The string line model used here is based on the Leica RoadRunner "RR_Stringlinelayers" \<Feature> extension but is renamed as "IM_Stringlinelayers".

The string line model is defined under \<Alignments> elements by adding the IM_StringlineLayers \<Feature> extension. The constituent line strings and their locations are set by layer in the IM_StringlineLayer \<Feature> child element. The alignments are identified by their unique name \<Alignment>.name, which are listed in the IM_StringlineLayer \<Feature> element, separated by commas. A layer shall be assigned with unique name, human readable description and a centerline. When describing a layered structure the layers of the string line model shall be assigned with category codes (with IM_Taxonomy \<Feature>). The same line string may belong to several different layers.

{{xtabulate2 IM_StringlineLayer_name--ltProperty--gt}}

{{xtabulate IM_StringlineLayer--ltFeature--gt}}

IM_StringLineLayer \<Feature>-data content:

- Comma separated list of alignment names defining a surface in left to right order

{{xtabulate2 IM_StringlineLayers_name--ltProperty--gt}}

{{xtabulate5 IM_StringlineLayers--ltFeature--gt}}


For further details see:  

- {{refsec mvd-stringlinemodel}}

### Cross-section parameter \<Feature> extension {#sec:mvd-crossectionparametersextension}

Cross-section parameters contain parametric information considered crucial for each route type. They are set for the stationing reference alignment in the <CrossSects>.<CrossSect> IM_CrossSect \<Feature> extension under the <Alignment> element. The chosen cross-section parameters are set in fields (\<Property>). It is recommended to describe all used parameters for each cross-section. If some parameters change, the cross-section where the parameter begins to change and the end of the transition are described.


The used \<Property> fields of IM_CrossSect vary by route type.

#### Road and street planning:

{{xtabulate2 IM_CrossSect_pavementClass--ltProperty--gt}}

{{xtabulate2 IM_CrossSect_pavementThickness--ltProperty--gt}}

{{xtabulate2 IM_CrossSect_loadCapacity--ltProperty--gt}}

For further details see {{refsec mvd-roadcrosssectparameters}}


#### Railway planning:

{{xtabulate2 IM_CrossSect_tracks--ltProperty--gt}}

{{xtabulate2 IM_CrossSect_trackDist--ltProperty--gt}}

{{xtabulate2 IM_CrossSect_thickness--ltProperty--gt}}

{{xtabulate2 IM_CrossSect_bedWidth--ltProperty--gt}}

For further details see {{refsec mvd-railcrosssections}}

#### Waterway planning:

{{xtabulate2 IM_CrossSect_depth--ltProperty--gt}}

{{xtabulate2 IM_CrossSect_width--ltProperty--gt}}

{{xtabulate2 IM_CrossSect_waterLevel--ltProperty--gt}}

For further details see {{refsec mvd-waterwaycrosssectionparameters}}


{{xtabulate5 IM_CrossSect--ltFeature--gt}}

### Water supply and sewerage - structure details \<Feature> extension {#sec:mvd-structuredetails}

Additional parameters for the water supply and sewerage network structures are described via IM_Struct \<Feature> extension.

{{xtabulate2 IM_Struct_rimDiameter--ltProperty--gt}}

{{xtabulate2 IM_Struct_rimCenter--ltProperty--gt}}

{{xtabulate2 IM_Struct_heightDeposit--ltProperty--gt}}

{{xtabulate2 IM_Struct_volumeDeposit--ltProperty--gt}}

{{xtabulate2 IM_Struct_rimType--ltProperty--gt}}

{{xtabulate2 IM_Struct_rimMaterial--ltProperty--gt}}

{{xtabulate2 IM_Struct_rimLoad--ltProperty--gt}}

{{xtabulate2 IM_Struct_equipmentCategory--ltProperty--gt}}

{{xtabulate2 IM_Struct_equipmentCode--ltProperty--gt}}

{{xtabulate5 IM_Struct--ltFeature--gt}}


For further details see:     	

- {{refsec mvd-circularstructure}}
- {{refsec mvd-rectangularstructures}}
- {{refsec mvd-pipeinletsandoutlets}}
- {{refsec mvd-pipeconnection}}
- {{refsec mvd-equipment}}

### Water supply and sewerage - pipe details \<Feature> extension {#sec:mvd-pipedetails}

Additional parameters for the water supply and sewerage network pipes are described via IM_Pipe \<Feature> extension.

{{xtabulate2 IM_Pipe_elevType--ltProperty--gt}}

{{xtabulate2 IM_Pipe_jointType--ltProperty--gt}}

{{xtabulate5 IM_Pipe--ltFeature--gt}}


For further details see:

- {{refsec mvd-circularpipes}}
- {{refsec mvd-eggpipes}}
- {{refsec mvd-ellipticpipe}}
- {{refsec mvd-rectangularpipe}}
- {{refsec mvd-channels}}


### Water supply and sewerage - Pipe network type \<Feature> extension {#sec:mvd-networkdetails}

When the pipe network type is other than one of those covered by the pipeNetType attribute of the <PipeNetwork> element, the optional IM_PipeNetworkType \<Feature> extension shall be used (with the pipeNetType attribute set to "other").

{{xtabulate2 IM_PipeNetwork_pipeNetworkType--ltProperty--gt}}

{{xtabulate5 IM_PipeNetworkType--ltFeature--gt}}


### Spatial allocation and avoidance - Spatial \<Feature> extension {#sec:mvd-spatialallocandavoidance}

{{xtabulate2 IM_PlanFeature_spatialAlloc--ltProperty--gt}}

{{xtabulate2 IM_PlanFeature_spatialAvoidance--ltProperty--gt}}

{{xtabulate5 IM_Spatial--ltFeature--gt}}
