#!/usr/bin/env python3
"""Genera en.html y fr.html a partir de index.html (español, versión de referencia).

Uso:  python3 tools/i18n.py

Cada entrada de TRANSLATIONS es (español, inglés, francés). El script se detiene
si un texto español ya no se encuentra en index.html: así nos damos cuenta
cuando el original cambió y hay que actualizar la traducción.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
BASE_URL = "https://thot-lab.github.io/chiribiquete-vr/"

# (es, en, fr) — de lo más largo a lo más corto: las frases antes que las palabras sueltas.
TRANSLATIONS = [
    # ---------- <head> ----------
    ("Chiribiquete VR — una experiencia inmersiva creada por NV Visuales y THOT. Exposición en la Alianza Francesa de Bogotá, sede Chicó, desde el 19 de noviembre de 2026.",
     "Chiribiquete VR — an immersive experience created by NV Visuales and THOT. Exhibition at the Alianza Francesa de Bogotá, Chicó branch, from 19 November 2026.",
     "Chiribiquete VR — une expérience immersive créée par NV Visuales et THOT. Exposition à l’Alliance Française de Bogotá, site de Chicó, à partir du 19 novembre 2026."),
    ('content="es_CO"', 'content="en_GB"', 'content="fr_FR"'),
    ("assets/meta/og-image-es.jpg", "assets/meta/og-image-en.jpg", "assets/meta/og-image-fr.jpg"),
    ("Chiribiquete VR sobre un paisaje aéreo de la Amazonia colombiana",
     "Chiribiquete VR over an aerial view of the Colombian Amazon",
     "Chiribiquete VR sur un paysage aérien de l’Amazonie colombienne"),
    ("Viaje inmersivo al corazón de la Amazonia colombiana",
     "An immersive journey into the heart of the Colombian Amazon",
     "Voyage immersif au cœur de l’Amazonie colombienne"),

    # ---------- Navegación ----------
    ("Saltar al contenido", "Skip to content", "Aller au contenu"),
    ('aria-label="Idioma"', 'aria-label="Language"', 'aria-label="Langue"'),
    ('aria-label="Secciones"', 'aria-label="Sections"', 'aria-label="Sections"'),
    ('<i aria-hidden="true"></i>Actualidad</a>', '<i aria-hidden="true"></i>News</a>', '<i aria-hidden="true"></i>Actualités</a>'),
    ('>Experiencia</a>', '>Experience</a>', '>Expérience</a>'),
    ('>Galería</a>', '>Gallery</a>', '>Galerie</a>'),
    ('>Autores</a>', '>Authors</a>', '>Auteurs</a>'),

    # ---------- Portada ----------
    ("Tepuy de Chiribiquete emergiendo de la selva amazónica",
     "Chiribiquete tepui rising from the Amazon rainforest",
     "Tepuy de Chiribiquete émergeant de la forêt amazonienne"),
    ("Huellas ancestrales de la Amazonia", "Ancestral traces of the Amazon", "Empreintes ancestrales d’Amazonie"),
    ('<i aria-hidden="true"></i>Actualidad</span>', '<i aria-hidden="true"></i>News</span>', '<i aria-hidden="true"></i>Actualités</span>'),
    ("Alianza Francesa · Sede Chicó", "Alianza Francesa · Chicó", "Alliance Française · Chicó"),
    ("Inauguración 19.11.2026", "Opening 19.11.2026", "Inauguration 19.11.2026"),
    ("Inauguración 30.10.2026", "Opening 30.10.2026", "Inauguration 30.10.2026"),

    # ---------- Proyecto ----------
    ("Prueba VR: navegación frente a los pictogramas",
     "VR test: navigating in front of the pictograms",
     "Test VR : navigation face aux pictogrammes"),
    ("Una experiencia inmersiva creada por NV Visuales y THOT. A través de realidad virtual, imagen 360°, fotografía, video y museografía digital, el público se adentra en el universo sagrado de los tepuyes, la selva y las pinturas rupestres de Chiribiquete. El objetivo es compartir la belleza y el conocimiento de Chiribiquete sin poner en riesgo su equilibrio.",
     "An immersive experience created by NV Visuales and THOT. Through virtual reality, 360° imagery, photography, video and digital museography, visitors enter the sacred world of the tepuis, the rainforest and the rock paintings of Chiribiquete. The aim is to share the beauty and knowledge of Chiribiquete without endangering its balance.",
     "Une expérience immersive créée par NV Visuales et THOT. Grâce à la réalité virtuelle, à l’image à 360°, à la photographie, à la vidéo et à la muséographie numérique, le public pénètre dans l’univers sacré des tepuys, de la forêt et des peintures rupestres de Chiribiquete. L’objectif est de partager la beauté et la connaissance de Chiribiquete sans mettre en péril son équilibre."),

    # ---------- Actualidad ----------
    ('<i class="pulse" aria-hidden="true"></i>Actualidad</p>', '<i class="pulse" aria-hidden="true"></i>News</p>', '<i class="pulse" aria-hidden="true"></i>Actualités</p>'),
    ("<dt>Fecha de inauguración</dt>", "<dt>Opening date</dt>", "<dt>Date d’inauguration</dt>"),
    ("<dt>Lugar de exposición</dt>", "<dt>Venue</dt>", "<dt>Lieu d’exposition</dt>"),
    ("<dt>Tiempo de exposición</dt>", "<dt>Exhibition dates</dt>", "<dt>Durée de l’exposition</dt>"),
    ("Jueves 19 de noviembre de 2026", "Thursday 19 November 2026", "Jeudi 19 novembre 2026"),
    ("Alianza Francesa de Bogotá, sede Chicó", "Alianza Francesa de Bogotá, Chicó branch", "Alliance Française de Bogotá, site de Chicó"),
    ("Del 19 de noviembre al 19 de diciembre de 2026", "19 November – 19 December 2026", "Du 19 novembre au 19 décembre 2026"),
    ("Viernes 30 de octubre de 2026", "Friday 30 October 2026", "Vendredi 30 octobre 2026"),
    ("Museo Rietberg, Gablerstrasse 15, Zúrich", "Museum Rietberg, Gablerstrasse 15, Zurich", "Musée Rietberg, Gablerstrasse 15, Zurich"),
    ("Del 30 de octubre de 2026 al 14 de marzo de 2027", "30 October 2026 – 14 March 2027", "Du 30 octobre 2026 au 14 mars 2027"),
    (">Agendar<", ">Add to calendar<", ">Ajouter à l’agenda<"),
    (">Cómo llegar<", ">Directions<", ">Itinéraire<"),
    ("Ver en el sitio del museo ↗", "View on the museum website ↗", "Voir sur le site du musée ↗"),
    # Agenda (texto codificado en la URL)
    ("Inauguraci%C3%B3n%20y%20conversatorio", "Opening%20and%20panel%20discussion", "Inauguration%20et%20table%20ronde"),
    ("Exposici%C3%B3n%20inmersiva%20Chiribiquete%20VR", "Immersive%20exhibition%20Chiribiquete%20VR", "Exposition%20immersive%20Chiribiquete%20VR"),
    ("El%20legado%20de%20la%20Amazon%C3%ADa%20%E2%80%94%20Museo%20Rietberg", "Amazonian%20Legacies%20%E2%80%94%20Museum%20Rietberg", "L%E2%80%99h%C3%A9ritage%20de%20l%E2%80%99Amazonie%20%E2%80%94%20Mus%C3%A9e%20Rietberg"),
    ("Instalaci%C3%B3n%20inmersiva%20Chiribiquete", "Immersive%20installation%20Chiribiquete", "Installation%20immersive%20Chiribiquete"),

    ("Chiribiquete VR llega a Bogotá en el marco de Novembre Numérique, el festival de las culturas digitales de la red de Alianzas Francesas, que celebra las nuevas formas interactivas del arte. Un evento de la Alianza Francesa de Bogotá, que acoge en la galería de su sede Chicó una exposición entre arte, ciencia y tecnología: realidad virtual, fotografía y museografía digital para adentrarse en los tepuyes, la selva y las pinturas rupestres de Chiribiquete. La inauguración estará acompañada de un conversatorio de alto nivel en el auditorio de la Alianza Francesa.",
     "Chiribiquete VR comes to Bogotá as part of Novembre Numérique, the festival of digital cultures of the Alliance Française network, which celebrates new interactive forms of art. An event of the Alianza Francesa de Bogotá, which hosts in the gallery of its Chicó branch an exhibition at the crossroads of art, science and technology: virtual reality, photography and digital museography to explore the tepuis, the rainforest and the rock paintings of Chiribiquete. The opening will be accompanied by a high-level panel discussion in the Alianza Francesa auditorium.",
     "Chiribiquete VR arrive à Bogotá dans le cadre de Novembre Numérique, le festival des cultures numériques du réseau des Alliances Françaises, qui célèbre les nouvelles formes interactives de l’art. Un événement de l’Alliance Française de Bogotá, qui accueille dans la galerie de son site de Chicó une exposition entre art, science et technologie&nbsp;: réalité virtuelle, photographie et muséographie numérique pour pénétrer dans les tepuys, la forêt et les peintures rupestres de Chiribiquete. L’inauguration sera accompagnée d’une table ronde de haut niveau dans l’auditorium de l’Alliance Française."),
    ("Socios &amp; apoyos", "Partners &amp; supporters", "Partenaires &amp; soutiens"),

    ("El legado de la Amazonia<span>Arte y arqueología</span>",
     "Amazonian Legacies<span>Art and archaeology</span>",
     "L’héritage de l’Amazonie<span>Art et archéologie</span>"),
    ("El Museo Rietberg de Zúrich dedica una gran exposición al arte y la arqueología de la Amazonia, habitada desde hace al menos 13&nbsp;000 años, donde naturaleza y cultura no se conciben por separado.",
     "The Museum Rietberg in Zurich is devoting a major exhibition to the art and archaeology of the Amazon, a region inhabited for at least 13,000 years, where nature and culture are not seen as separate.",
     "Le Musée Rietberg de Zurich consacre une grande exposition à l’art et à l’archéologie de l’Amazonie, habitée depuis au moins 13&nbsp;000 ans, où nature et culture ne sont pas pensées séparément."),
    ('En ella, THOT presenta una instalación digital monumental coproducida por Un film à la patte y el Museo Rietberg. La experiencia fue realizada con ',
     'There, THOT presents a monumental digital installation co-produced by Un film à la patte and the Museum Rietberg. The experience was created with ',
     'THOT y présente une installation numérique monumentale coproduite par Un film à la patte et le Musée Rietberg. L’expérience a été réalisée avec '),
    ('</a> y vio la luz gracias a la movilización de numerosos talentos, entre ellos Vladimir Bodnartchouk, ',
     '</a> and came to life thanks to many talented people, including Vladimir Bodnartchouk, ',
     '</a> et a vu le jour grâce à la mobilisation de nombreux talents, notamment Vladimir Bodnartchouk, '),
    ('</a> y <a href="https://www.colinidier.com"',
     '</a> and <a href="https://www.colinidier.com"',
     '</a> et <a href="https://www.colinidier.com"'),
    ('</a>. Los invitamos a descubrir el sitio arqueológico de Chiribiquete, en Colombia, sus inmensas montañas llamadas tepuyes y las innumerables y misteriosas pinturas rupestres que albergan. Bienvenidos al corazón de la Amazonia…',
     '</a>. We invite you to discover the archaeological site of Chiribiquete in Colombia, its immense mountains known as tepuis, and the countless mysterious rock paintings they shelter. Welcome to the heart of the Amazon…',
     '</a>. Nous vous invitons à y découvrir le site archéologique de Chiribiquete, en Colombie, ses immenses montagnes appelées tepuys et les innombrables et mystérieuses peintures rupestres qu’elles abritent. Bienvenue au cœur de l’Amazonie…'),
    ("32 m de pantallas en triángulo", "32 m of screens in a triangle", "32 m d’écrans en triangle"),
    ("Muro 1 de la instalación: pared de roca de Chiribiquete con el título", "Installation wall 1: Chiribiquete rock face with the title", "Mur 1 de l’installation : paroi rocheuse de Chiribiquete avec le titre"),
    ("Muro 2 de la instalación: panorama aéreo de los tepuyes", "Installation wall 2: aerial panorama of the tepuis", "Mur 2 de l’installation : panorama aérien des tepuys"),
    ("Muro 3 de la instalación: pictogramas rupestres sobre fondo negro", "Installation wall 3: rock-art pictograms on a black background", "Mur 3 de l’installation : pictogrammes rupestres sur fond noir"),

    # ---------- La experiencia ----------
    (">La experiencia</p>", ">The experience</p>", ">L’expérience</p>"),
    ("Propósito general de la exposición", "General purpose of the exhibition", "Propos général de l’exposition"),
    ("El envejecimiento de nuestra litosfera deja huellas tan enigmáticas como gigantescas. La meseta de las Guayanas, que se extiende por el norte de América Latina, se formó en el Precámbrico y es uno de los macizos más antiguos del planeta: algunas partes tienen más de 2.000 millones de años. Se les conoce como tepuyes, majestuosas formaciones geológicas que se alzan en medio de la selva amazónica y que han inspirado a la humanidad durante miles de años, tanto que aquí han grabado sus historias, sus sueños y sus mitos.",
     "The ageing of our lithosphere leaves traces as enigmatic as they are gigantic. The Guiana Shield, which stretches across northern Latin America, formed in the Precambrian and is one of the oldest massifs on the planet: some parts are more than 2 billion years old. They are known as tepuis, majestic geological formations that rise from the middle of the Amazon rainforest and have inspired humanity for thousands of years — so much so that people recorded their stories, their dreams and their myths here.",
     "Le vieillissement de notre lithosphère laisse des traces aussi énigmatiques que gigantesques. Le plateau des Guyanes, qui s’étend au nord de l’Amérique latine, s’est formé au Précambrien et compte parmi les plus anciens massifs de la planète&nbsp;: certaines parties ont plus de 2 milliards d’années. On les appelle tepuys, majestueuses formations géologiques qui se dressent au milieu de la forêt amazonienne et inspirent l’humanité depuis des milliers d’années, au point que les hommes y ont inscrit leurs histoires, leurs rêves et leurs mythes."),
    ("En el Parque de Chiribiquete (Colombia), en los acantilados de los tepuyes, se han identificado más de 75.000 pinturas rupestres. Su existencia y conservación llevan muchos misterios, incluyendo aquellos relacionados con las vías de migración humana en el continente americano.",
     "In Chiribiquete National Park (Colombia), more than 75,000 rock paintings have been identified on the cliffs of the tepuis. Their existence and preservation hold many mysteries, including those related to the routes of human migration across the American continent.",
     "Dans le parc de Chiribiquete (Colombie), plus de 75&nbsp;000 peintures rupestres ont été recensées sur les falaises des tepuys. Leur existence et leur conservation recèlent de nombreux mystères, notamment ceux liés aux routes de migration humaine sur le continent américain."),
    ("Estas fascinantes pinturas combinan pictogramas abstractos y figurativos. Parecen recrear momentos fundadores de la mitología ancestral, de las prácticas chamánicas. Presentan toda una gama de megafauna amazónica extinguida, una vida cotidiana de caza y pesca, danzas y rituales…",
     "These fascinating paintings combine abstract and figurative pictograms. They seem to re-enact founding moments of ancestral mythology and shamanic practices. They depict a whole range of extinct Amazonian megafauna, a daily life of hunting and fishing, dances and rituals…",
     "Ces fascinantes peintures associent pictogrammes abstraits et figuratifs. Elles semblent rejouer des moments fondateurs de la mythologie ancestrale et des pratiques chamaniques. On y découvre toute une mégafaune amazonienne disparue, une vie quotidienne faite de chasse et de pêche, de danses et de rituels…"),
    ("Pintado hace miles de años, este arte rupestre es aún más valioso por ser inaccesible. Esta parte de la selva es totalmente prohibida. En este inmenso territorio, aún viven grupos étnicos en aislación total y voluntaria, que parecen utilizar y conservar aún las pinturas realizadas por los pueblos de ayer.",
     "Painted thousands of years ago, this rock art is all the more precious for being inaccessible. This part of the rainforest is strictly off-limits. In this immense territory, ethnic groups still live in total and voluntary isolation, and seem to still use and preserve the paintings made by the peoples of the past.",
     "Peint il y a des milliers d’années, cet art rupestre est d’autant plus précieux qu’il est inaccessible. Cette partie de la forêt est totalement interdite. Sur cet immense territoire vivent encore des groupes ethniques en isolement total et volontaire, qui semblent toujours utiliser et préserver les peintures réalisées par les peuples d’hier."),
    ("Un puñado de científicos comenzó sus investigaciones hace unos cuarenta años, pero los secretos susurrados al pie de los tepuyes permanecen diligentemente guardados.",
     "A handful of scientists began their research some forty years ago, but the secrets whispered at the foot of the tepuis remain carefully guarded.",
     "Une poignée de scientifiques a entamé ses recherches il y a une quarantaine d’années, mais les secrets murmurés au pied des tepuys restent jalousement gardés."),
    ("Embárquese en una misión científica en el corazón de la Amazonia", "Embark on a scientific mission into the heart of the Amazon", "Embarquez pour une mission scientifique au cœur de l’Amazonie"),

    ("Objetivos culturales de la exposición", "Cultural objectives of the exhibition", "Objectifs culturels de l’exposition"),
    ("Como en el caso de las famosas cuevas francesas, prohibir el acceso a un sitio de gran valor patrimonial y cultural sugiere la realización de una réplica, para que las riquezas y los conocimientos adquiridos puedan ser compartidos. La exposición propuesta pretende ser la primera réplica inmersiva de Chiribiquete, en línea con la política colombiana de «conocer sin ir».",
     "As with the famous French caves, closing a site of great heritage and cultural value to the public calls for a replica, so that its riches and the knowledge gained can be shared. The proposed exhibition aims to be the first immersive replica of Chiribiquete, in line with Colombia’s policy of “knowing without going”.",
     "Comme pour les célèbres grottes françaises, interdire l’accès à un site d’une grande valeur patrimoniale et culturelle invite à en réaliser une réplique, afin que ses richesses et les connaissances acquises puissent être partagées. L’exposition proposée se veut la première réplique immersive de Chiribiquete, dans la lignée de la politique colombienne du «&nbsp;connaître sans y aller&nbsp;»."),
    ("La exposición puede adaptarse a diferentes orientaciones museográficas, abarcando los siguientes temas:",
     "The exhibition can be adapted to different museographic approaches, covering the following themes:",
     "L’exposition peut s’adapter à différentes orientations muséographiques et aborder les thèmes suivants&nbsp;:"),
    ("Antropología, arqueología, etnografía, interpretación comparada del arte rupestre, chamanismo;",
     "Anthropology, archaeology, ethnography, comparative interpretation of rock art, shamanism;",
     "Anthropologie, archéologie, ethnographie, interprétation comparée de l’art rupestre, chamanisme&nbsp;;"),
    ("Ecología, geología y biología;", "Ecology, geology and biology;", "Écologie, géologie et biologie&nbsp;;"),
    ("Prehistoria e historia;", "Prehistory and history;", "Préhistoire et histoire&nbsp;;"),
    ("Cambio climático y protección de la biodiversidad.", "Climate change and biodiversity protection.", "Changement climatique et protection de la biodiversité."),

    ("Medios artísticos / Museografía / Innovación", "Artistic media / Museography / Innovation", "Moyens artistiques / Muséographie / Innovation"),
    ("La aventura inmersiva propuesta es el resultado de una cooperación sin precedentes entre un equipo de producción y creación de documentales (Un film à la patte — ",
     "The proposed immersive adventure is the result of an unprecedented collaboration between a documentary production and creation team (Un film à la patte — ",
     "L’aventure immersive proposée est le fruit d’une coopération inédite entre une équipe de production et de création documentaire (Un film à la patte — "),
    (") y un innovador equipo de creación de exposiciones, utilizando tecnología de realidad virtual (NV Visuales — ",
     ") and an innovative exhibition design team working with virtual reality technology (NV Visuales — ",
     ") et une équipe innovante de création d’expositions utilisant la technologie de la réalité virtuelle (NV Visuales — "),
    (" Ver el sitio del documental: ", " See the documentary website: ", " Voir le site du documentaire&nbsp;: "),
    ("La escenografía puede adaptarse al lugar de exposición y desplegarse en varios soportes, en función de las necesidades museográficas. Prevé fotografías de gran formato, proyecciones de video de diversos tipos, el uso de tecnología de realidad virtual (VR) en varios formatos: estaciones de teletransporte con cascos VR, pantallas táctiles y proyectores video. La realidad virtual permite transportar al usuario a escenas de 360° de alta definición, con sonido en tres dimensiones, dentro de las cuales se pueden activar elementos multimedia: secuencias de video, entrevistas, fotografías, testimonios de audio, animaciones. Las secuencias de video son producidas y realizadas por un equipo cinematográfico de excelencia televisiva.",
     "The scenography can be adapted to the exhibition venue and deployed across several media, depending on museographic needs. It includes large-format photographs, video projections of various kinds, and virtual reality (VR) technology in several formats: teleportation stations with VR headsets, touch screens and video projectors. Virtual reality transports users into high-definition 360° scenes with three-dimensional sound, in which multimedia elements can be activated: video sequences, interviews, photographs, audio testimonies, animations. The video sequences are produced and directed by a film crew from the world of top-tier television.",
     "La scénographie peut s’adapter au lieu d’exposition et se déployer sur plusieurs supports, selon les besoins muséographiques. Elle prévoit des photographies grand format, des projections vidéo de différents types et l’usage de la réalité virtuelle (VR) sous plusieurs formes&nbsp;: stations de téléportation avec casques VR, écrans tactiles et vidéoprojecteurs. La réalité virtuelle transporte l’utilisateur dans des scènes à 360° en haute définition, avec un son en trois dimensions, au sein desquelles des éléments multimédias peuvent être activés&nbsp;: séquences vidéo, entretiens, photographies, témoignages sonores, animations. Les séquences vidéo sont produites et réalisées par une équipe cinématographique issue de l’excellence télévisuelle."),
    ("El visitante viaja de escenario en escenario, explorando y apropiándose de los temas a su propio ritmo. Tiene la sensación de estar él mismo dentro del parque Chiribiquete con interacción con los científicos. Los elementos de interacción le permiten pasar del estatus de espectador al estatus de explorador.",
     "Visitors travel from scene to scene, exploring and taking ownership of the themes at their own pace. They feel as if they were inside Chiribiquete park themselves, interacting with the scientists. The interactive elements allow them to move from spectator to explorer.",
     "Le visiteur voyage de scène en scène, explore et s’approprie les thèmes à son rythme. Il a le sentiment d’être lui-même au cœur du parc de Chiribiquete, en interaction avec les scientifiques. Les éléments d’interaction lui permettent de passer du statut de spectateur à celui d’explorateur."),
    ("Visitante en la estación VR de la instalación", "Visitor at the installation’s VR station", "Visiteur à la station VR de l’installation"),
    (">Públicos</p>", ">Audiences</p>", ">Publics</p>"),
    ("Museos, universidades, centros culturales, instituciones públicas, embajadas, fundaciones, festivales y espacios dedicados a la cultura, la educación ambiental y patrimonial y el arte.",
     "Museums, universities, cultural centres, public institutions, embassies, foundations, festivals and venues dedicated to culture, environmental and heritage education, and the arts.",
     "Musées, universités, centres culturels, institutions publiques, ambassades, fondations, festivals et lieux consacrés à la culture, à l’éducation environnementale et patrimoniale et à l’art."),

    # ---------- Galería ----------
    (">Galería</p>", ">Gallery</p>", ">Galerie</p>"),
    ('alt="Vista aérea de los tepuyes de Chiribiquete"', 'alt="Aerial view of the Chiribiquete tepuis"', 'alt="Vue aérienne des tepuys de Chiribiquete"'),
    ('alt="Paisaje de Chiribiquete fotografiado por Nicolas Villaume"', 'alt="Chiribiquete landscape photographed by Nicolas Villaume"', 'alt="Paysage de Chiribiquete photographié par Nicolas Villaume"'),
    ('alt="Detalle del paisaje amazónico de Chiribiquete"', 'alt="Detail of the Amazonian landscape of Chiribiquete"', 'alt="Détail du paysage amazonien de Chiribiquete"'),
    ('alt="Abrigo rocoso y pinturas rupestres de Chiribiquete"', 'alt="Rock shelter and rock paintings of Chiribiquete"', 'alt="Abri sous roche et peintures rupestres de Chiribiquete"'),
    ('alt="Interfaz VR sobre pinturas rupestres de Chiribiquete"', 'alt="VR interface over Chiribiquete rock paintings"', 'alt="Interface VR sur les peintures rupestres de Chiribiquete"'),
    ('alt="Pinturas rupestres de Chiribiquete"', 'alt="Rock paintings of Chiribiquete"', 'alt="Peintures rupestres de Chiribiquete"'),
    ('alt="Interfaz VR sobre paisaje amazónico y deforestación"', 'alt="VR interface over an Amazonian landscape and deforestation"', 'alt="Interface VR sur un paysage amazonien et la déforestation"'),

    # ---------- Autores ----------
    (">Autores</p>", ">Authors</p>", ">Auteurs</p>"),
    ('Nicolas Villaume es un fotógrafo galardonado y National Geographic Explorer con más de 25 años de trayectoria internacional. Especialista en narrativas inmersivas (<em>immersive storytelling</em>), fundó en 2004 la organización Conversations du Monde, dedicada a crear experiencias multimedia que promueven la conciencia y la valoración de la diversidad biocultural.',
     'Nicolas Villaume is an award-winning photographer and National Geographic Explorer with more than 25 years of international experience. A specialist in immersive storytelling, he founded Conversations du Monde in 2004, an organization dedicated to creating multimedia experiences that raise awareness and appreciation of biocultural diversity.',
     'Nicolas Villaume est un photographe primé et National Geographic Explorer, fort de plus de 25 ans de carrière internationale. Spécialiste des récits immersifs (<em>immersive storytelling</em>), il fonde en 2004 l’organisation Conversations du Monde, dédiée à la création d’expériences multimédias qui sensibilisent à la diversité bioculturelle et la mettent en valeur.'),
    ('Su trabajo, que abarca desde comunidades árticas afectadas por el cambio climático hasta culturas ancestrales de la Amazonia colombiana, explora las conexiones entre naturaleza y cultura, buscando acercar al público a estos territorios y sus comunidades e inspirar nuevas formas de conciencia y acción.',
     'His work, ranging from Arctic communities affected by climate change to ancestral cultures of the Colombian Amazon, explores the connections between nature and culture, seeking to bring audiences closer to these territories and their communities and to inspire new forms of awareness and action.',
     'Son travail, des communautés arctiques touchées par le changement climatique aux cultures ancestrales de l’Amazonie colombienne, explore les liens entre nature et culture, avec l’ambition de rapprocher le public de ces territoires et de leurs communautés, et d’inspirer de nouvelles formes de conscience et d’action.'),
    ('Su obra ha sido presentada en más de 50 exposiciones internacionales, incluyendo el Smithsonian National Museum of the American Indian, la sede de las Naciones Unidas y el Museo Nacional de Dinamarca, así como en importantes encuentros internacionales sobre el clima.',
     'His work has been shown in more than 50 international exhibitions, including at the Smithsonian National Museum of the American Indian, the United Nations headquarters and the National Museum of Denmark, as well as at major international climate gatherings.',
     'Son œuvre a été présentée dans plus de 50 expositions internationales, notamment au Smithsonian National Museum of the American Indian, au siège des Nations unies et au Musée national du Danemark, ainsi que lors de grandes rencontres internationales consacrées au climat.'),
    ('alt="Embajada de Francia en Colombia"', 'alt="Embassy of France in Colombia"', 'alt="Ambassade de France en Colombie"'),
    ("Ver en Instagram ↗", "View on Instagram ↗", "Voir sur Instagram ↗"),
    ('Laurent Pacoud es ingeniero ambiental y emprendedor. Ha trabajado en los desafíos del desarrollo sostenible y del cambio climático en más de veinte países. Tras quince años en la cooperación internacional, fundó la empresa THOT, cuyas actividades cruzan ciencia, política y arte.',
     'Laurent Pacoud is an environmental engineer and entrepreneur. He has worked on sustainable development and climate change issues in more than twenty countries. After fifteen years in international cooperation, he founded THOT, a company whose activities bring together science, policy and art.',
     'Laurent Pacoud est ingénieur en environnement et entrepreneur. Il a travaillé sur les enjeux du développement durable et du changement climatique dans plus de vingt pays. Après quinze années dans la coopération internationale, il a fondé la société THOT, dont les activités croisent science, politique et art.'),
    ('Junto a Nicolas Villaume, impulsa y coordina experiencias inmersivas que combinan divulgación científica y sensibilización sobre la preservación de los ecosistemas.',
     'Together with Nicolas Villaume, he initiates and coordinates immersive experiences that combine science outreach with raising awareness about ecosystem preservation.',
     'Avec Nicolas Villaume, il initie et coordonne des expériences immersives qui mêlent vulgarisation scientifique et sensibilisation à la préservation des écosystèmes.'),

    # ---------- Pie de página y diálogo ----------
    ("Una realización de NV Visuales y THOT", "A production by NV Visuales and THOT", "Une réalisation de NV Visuales et THOT"),
    ("Fotografías © Nicolas Villaume", "Photographs © Nicolas Villaume", "Photographies © Nicolas Villaume"),
    ('aria-label="Imagen ampliada"', 'aria-label="Enlarged image"', 'aria-label="Image agrandie"'),
    ('aria-label="Cerrar"', 'aria-label="Close"', 'aria-label="Fermer"'),

    # ---------- Nombres propios, al final ----------
    ("Museo Rietberg", "Museum Rietberg", "Musée Rietberg"),
    ("Zúrich", "Zurich", "Zurich"),
    ("Alianza Francesa", "Alianza Francesa", "Alliance Française"),
]

LANGS = {
    "en": {"col": 1, "file": "en.html", "url": BASE_URL + "en.html", "manifest_lang": "en"},
    "fr": {"col": 2, "file": "fr.html", "url": BASE_URL + "fr.html", "manifest_lang": "fr"},
}


def build(code, cfg):
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    missing = []
    for row in TRANSLATIONS:
        es, target = row[0], row[cfg["col"]]
        if es not in html:
            missing.append(es)
            continue
        html = html.replace(es, target)
    if missing:
        sys.exit(f"[{code}] Textos no encontrados en index.html (¿cambió el original?):\n  - " + "\n  - ".join(m[:90] for m in missing))

    html = html.replace('<html lang="es">', f'<html lang="{code}">', 1)
    html = html.replace(f'<link rel="canonical" href="{BASE_URL}" />', f'<link rel="canonical" href="{cfg["url"]}" />', 1)
    html = html.replace(f'<meta property="og:url" content="{BASE_URL}" />', f'<meta property="og:url" content="{cfg["url"]}" />', 1)
    # Bandera activa
    html = html.replace(' title="Español" aria-current="page"', ' title="Español"', 1)
    html = html.replace(f'href="{cfg["file"]}" hreflang="{code}" lang="{code}" title="',
                        f'href="{cfg["file"]}" hreflang="{code}" lang="{code}" aria-current="page" title="', 1)
    html = html.replace('<!DOCTYPE html>', '<!DOCTYPE html>\n<!-- Generado por tools/i18n.py a partir de index.html: no editar a mano. -->', 1)
    (ROOT / cfg["file"]).write_text(html, encoding="utf-8")
    print(f"✓ {cfg['file']}")


if __name__ == "__main__":
    for code, cfg in LANGS.items():
        build(code, cfg)
