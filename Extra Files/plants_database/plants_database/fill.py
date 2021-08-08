#this is meant to fill the database with data
from plant_base.models import Plants, Berries, Flowers, Stems, Leaves


#empties the database first
Plants.objects.all().delete()
Leaves.objects.all().delete()
Flowers.objects.all().delete()
Berries.objects.all().delete()
Stems.objects.all().delete()


#American Fox Sedge 1
Plants(name = 'American Fox Sedge', latin_name= 'Carex Vulpinoidea', image_name= 'American_Fox_Sedge_Plant.jpg').save()
plant = Plants.objects.filter(name= 'American Fox Sedge').first()
Stems(plant= plant, desc= '1 meter, Grass').save()
Leaves(plant= plant, shapes='LI', desc= 'Long blades from the bottom of the plant').save()
Berries(plant= plant, colors= 'Red-Brown', desc = 'spiky, at the top of the stem, 5-10cm long', image_name= 'American_Fox_Sedge_Seedhead.jpg').save()
print(plant.name + ' Complete!!!')

#Asperagus 2
Plants(name = 'Asperagus', latin_name= 'Asparagus officinalis', isNative= False, image_name= 'Asparagus_Sprouts.jpg').save()
plant = Plants.objects.filter(name= 'Asperagus').first()
Stems(plant= plant, desc= '2 meters, Resembles store bought asparagus, develops alternate branches').save()
Leaves(plant= plant, shapes='DL', desc= 'Small, alternating, scale like').save()
Berries(plant= plant, colors= 'Green, Red', desc = 'Green berries 1cm across that ripen to red', image_name= 'Asparagus_Growing_Seeds.jpg').save()
print(plant.name + ' Complete!!!')

#Barnyard Grass 3
Plants(name = 'Barnyard Grass', latin_name= 'Echinochloa crus-galli', isNative= False, image_name= 'Barnyard_Grass_Leaves.jpg').save()
plant = Plants.objects.filter(name= 'Barnyard Grass').first()
Stems(plant= plant, desc= 'Grass').save()
Leaves(plant= plant, shapes='LI', desc= 'Long 50cm leaves from the bottom of the plant that roll into the stem', image_name= 'Barnyard_Grass_Leaves.jpg').save()
Berries(plant= plant, desc = 'Multiple seed heads, 10-40cm, made of several small spikelets', image_name= 'Barnyard_Grass_Seedhead.jpg').save()
print(plant.name + ' Complete!!!')

#Bittersweet Nightshade 4
Plants(name= 'Bittersweet Nightshade', latin_name= 'Solanum dulcamara', isNative= False, image_name= 'Bittersweet_Nightshade_Leaves.jpg').save()
plant = Plants.objects.filter(name= 'Bittersweet Nightshade').first()
Stems(plant= plant, desc= 'Vine, Woody lower stem').save()
Leaves(plant = plant, shapes= 'TL', desc= 'main leaf is 2-10cm long with a smaller leaf below it on each side', image_name= 'Bittersweet_Nightshade_Leaves.jpg').save()
Flowers(plant= plant, colors= 'Purple', desc= 'star shaped, yellow center cone', image_name= 'Bittersweet_Nightshade_Flowers_Berries.jpg').save()
Berries(plant= plant, colors= 'Red, Green', desc= 'egg-shaped berries', image_name= 'Bittersweet_Nightshade_Flowers_Berries.jpg').save()
print(plant.name + ' Complete!!!')

#Black-Eyed Susan 5
Plants(name= 'Black-Eyed Susan', latin_name= 'Rudbeckia hirta', image_name= 'Black_Eyed_Susan_Plant.jpg').save()
plant = Plants.objects.filter(name= 'Black-Eyed Susan').first()
Stems(plant= plant, desc= '0.3-1 meter, Green, round').save()
Leaves(plant=plant, shapes= 'OL', desc= 'has a pointed end, irregularly placed, 5-18cm long').save()
Flowers(plant= plant, colors= 'Yellow', desc= 'brown center, 5-8cm wide', image_name= 'Black_Eyed_Susan_Flower.jpg').save()
print(plant.name + ' Complete!!!')

#Birdsfoot Trefoil 6
Plants(name= 'Birdsfoot Trefoil', latin_name= 'Lotus corniculatus', isNative= False, image_name= 'Birdsfoot_Trefoil_Plant.jpg').save()
plant = Plants.objects.filter(name= 'Birdsfoot Trefoil').first()
Stems(plant= plant, desc= '0.3-0.6 meters, Green, round').save()
Leaves(plant=plant, shapes= 'TL', desc= 'at the end of the stem with two more at the base, resembling a bird\'s foot', image_name= 'Birdsfoot_Trefoil_Leaves.jpg').save()
Flowers(plant= plant, colors= 'Yellow', desc= 'pea shaped, in clusters of 2-12', image_name= 'Birdsfoot_Trefoil_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Bladder Campion 7
Plants(name= 'Bladder Campion', latin_name= 'Silene vulgaris', isNative= False, image_name= 'Bladder_Campion_Flowers.jpg').save()
plant = Plants.objects.filter(name= 'Bladder Campion').first()
Stems(plant= plant, desc= 'Up to 0.6 meters, Pale Green, hairless').save()
Leaves(plant=plant, shapes= 'LA, OB', desc= 'Pale green to grayish green, opposite, 6cm long and 1.5cm across', image_name= 'Bladder_Campion_Leaves.jpg').save()
Flowers(plant= plant, colors= 'White', desc= 'White petals with a white-pink bulb at the base, 1-1.5cm across', image_name= 'Bladder_Campion_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Blue Vervain 8
Plants(name= 'Blue Vervain', latin_name= 'Verbena hastata', image_name= 'Blue_Vervain_Flowers.jpg').save()
plant = Plants.objects.filter(name= 'Blue Vervain').first()
Stems(plant= plant, desc= '0.6-2 meters, White furred, square').save()
Leaves(plant=plant, shapes= 'LA', desc= 'Serrated edges, 15cm long and 2.5cm wide', image_name= 'Blue_Vervain_Stem_Leaves.jpg').save()
Flowers(plant= plant, colors= 'Purple-Blue', desc= 'at or near top of stem', image_name= 'Blue_Vervain_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Burdock 9
Plants(name= 'Burdock', latin_name= 'Arctium minus, Arctium lappa', isNative= False, image_name= 'Burdock_Leaves.jpg').save()
plant = Plants.objects.filter(name= 'Burdock').first()
Stems(plant= plant, desc= '1.5 meters, Green-grey, round').save()
Leaves(plant=plant, shapes= 'HT', desc= 'Large leaves, 50cm long and 40cm wide', image_name= 'Burdock_Leaves.jpg').save()
Flowers(plant= plant, colors= 'Purple', desc= 'Purple flower extending from green-brown Velcro-like ball', image_name= 'Burdock_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Buttercup 10
Plants(name= 'Buttercup', latin_name= 'Ranunculus spp.', image_name= 'Buttercup_Leaves_Flower.jpg').save()
plant = Plants.objects.filter(name= 'Buttercup').first()
Stems(plant= plant, desc= '0.3 meters, Pale green, round').save()
Leaves(plant=plant, shapes= 'TL', desc= 'Dark green with three sections, each being toothed', image_name= 'Buttercup_Leaves_Flower.jpg').save()
Flowers(plant= plant, colors= 'Yellow', desc= 'has five petals, small', image_name= 'Buttercup_Leaves_Flower.jpg').save()
print(plant.name + ' Complete!!!')

#Canada Thistle 11
Plants(name= 'Canada Thistle', latin_name= 'Cirsium arvense', isNative= False, image_name= 'Canada_Thistle_Plant.jpg').save()
plant = Plants.objects.filter(name= 'Canada Thistle').first()
Stems(plant= plant, desc= '0.3-1.2 meters, Grooved and erect').save()
Leaves(plant=plant, shapes= 'LB', desc= 'spiny margins, alternate, bases surround the stem').save()
Flowers(plant= plant, colors= 'Pink, Purple', desc= 'growing from a bulb with spineless bracts', image_name= 'Canada_Thistle_Flower.jpg').save()
print(plant.name + ' Complete!!!')

#Carpetweed 12
Plants(name= 'Carpetweed', latin_name= 'Mollugo verticillata', isNative= False, image_name= 'Carpetweed_Plant.jpg').save()
plant = Plants.objects.filter(name= 'Carpetweed').first()
Stems(plant= plant, desc= 'Low to the ground in circular mats, viny').save()
Leaves(plant=plant, shapes= 'OL', desc= 'Rounded above and narrow at base, in groups of 3-8, 1-3cm long and <1cm wide').save()
Flowers(plant= plant, colors= 'White, Green-White', desc= '4-5mm across, in clusters of 2-5 where leaf meets stem', image_name= 'Carpetweed_Flowers.jpg').save()
Berries(plant= plant, desc= '0.5mm, kidney shaped').save()
print(plant.name + ' Complete!!!')

#Cattail 13
Plants(name= 'Cattail', latin_name= 'Typha latifolia', isNative= False, image_name= 'Cattail_Plant.jpg').save()
plant = Plants.objects.filter(name= 'Cattail').first()
Stems(plant= plant, desc= '1-3meters, Long, reedy, with spike at the top and brown sausage-like flowerhead below it').save()
Leaves(plant=plant, shapes= 'LA', desc= 'Long, attached at the base of the plan').save()
Flowers(plant= plant, colors= 'Brown', desc= 'sausage-like at top of stem', image_name= 'Cattail_Heads.jpg').save()
Berries(plant= plant, desc= 'Minute, attached to long fine hairs').save()
print(plant.name + ' Complete!!!')

#Chickweed 14
name = 'Chickweed'
Plants(name= name, latin_name= 'Stellaria media', isNative= False, image_name= 'Chickweed_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '0.4 meters, Smooth with 1-2 rows of hair').save()
Leaves(plant=plant, shapes= 'DL', desc= 'Opposite, rounded to egg shaped, pointed at apex').save()
Flowers(plant= plant, colors= 'White', desc= 'small, deeply lobed petals', image_name= 'Chickweed_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Chicory 15
name = 'Chicory'
Plants(name= name, latin_name= 'Cichorium intybus', isNative= False, image_name= 'Chicory_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '0.3-1.5 meters, Hairy lower, leafless upper, milky sap when cut').save()
Leaves(plant=plant, shapes= 'LA', desc= '10-32cm long and 2-8cm wide').save()
Flowers(plant= plant, colors= 'Blue', desc= 'in clusters of 1-4 on upper stems', image_name= 'Chicory_Flower.jpg').save()
print(plant.name + ' Complete!!!')

#Chinese Bugleweed 16
name = 'Chinese Bugleweed'
Plants(name= name, latin_name= 'Lycopus lucidus', isNative= False, image_name= 'Chinese_Bugleweed_Flowers.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '1 meter, Green, round').save()
Leaves(plant=plant, shapes= 'LI', desc= '10-15cm long in opposite pairs up the stem', image_name= 'Chinese_Bugleweed_Leaves.jpg').save()
Flowers(plant= plant, colors= 'White', desc= 'small, where stem and leaves meet', image_name= 'Chinese_Bugleweed_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Common Boneset 17
name = 'Common Boneset'
Plants(name= name, latin_name= 'Eupatorium perfoliatum', image_name= 'Common_Boneset_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '0.6-1.2 meters, Covered in long white hairs').save()
Leaves(plant=plant, shapes= 'AR', desc= 'Light yellow-green, opposite pairs, wrap around the stem, 5-20cm long and 5cm wide', image_name= 'Common_Boneset_Leaves_Stem.jpg').save()
Flowers(plant= plant, colors= 'White', desc= 'at ends of stems, in clusters 5-20cm across, each flower 0.5cm').save()
print(plant.name + ' Complete!!!')

#Common Lambsquarters 18
name = 'Common Lambsquarters'
Plants(name= name, latin_name= 'Chenopodium album', image_name= 'Common_Lambsquarters_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= 'Up to 1 meter, Erect, branching, hairless, vertically ridged, maroon striped').save()
Leaves(plant=plant, shapes= 'LA', desc= 'alternate, 3-10cm long with irregular teeth').save()  #Petioled not in database
Flowers(plant= plant, colors= 'Green', desc= 'small, dense clusters, on spikes', image_name= 'Common_Lambsquarters_Flowers.jpg').save()
Berries(plant= plant, colors= 'Brown',desc= '1-2mm').save()
print(plant.name + ' Complete!!!')

#Common Plantain 19
name = 'Common Plantain'
Plants(name= name, latin_name= 'Plantago major', isNative= False, image_name= 'Common_Plantain_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '0.1 meters, long central stalk').save()
Leaves(plant=plant, shapes= 'OL', desc= 'Large, at the base of the plant, with thick stems').save()
Flowers(plant= plant, colors= 'Green', desc= 'very small').save()
print(plant.name + ' Complete!!!')

#Common Ragweed 20
name = 'Common Ragweed'
Plants(name= name, latin_name= 'Ambrosia artemisiifolia', image_name= 'Common_Ragweed_Leaves.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '0.3-1 meter, Long rough hairs').save()
Leaves(plant=plant, shapes= 'CP', desc= 'Hairy to smooth, egg shaped, once or twice compound, alternate, 4-10cm long', image_name= 'Common_Ragweed_Leaves.jpg').save()
Flowers(plant= plant, colors= 'Green', desc= '2-3mm, inconspicuous, on terminal branches', image_name= 'Common_Ragweed_Flower.jpg').save()
Berries(plant= plant, desc= 'Longitudinal ridges with spines').save()
print(plant.name + ' Complete!!!')

#Common Soapwort 21
name = 'Common Soapwort'
Plants(name= name, latin_name= 'Saponaria officinalis', isNative= False, image_name= 'Common_Soapwort_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '0.3-0.8 meters, Round, hairless').save()
Leaves(plant=plant, shapes= 'OL, LA', desc= 'Opposite, ovate or broadly lanceolate, hairless, three veins, 10cm long and 4.5cm across', image_name= 'Common_Soapwort_Leaves.jpg').save()
Flowers(plant= plant, colors= 'Pink', desc= 'in groups at the end of the stems, 2cm across', image_name= 'Common_Soapwort_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Common Sorrel 22
name = 'Common Sorrel'
Plants(name= name, latin_name= 'Rumex acetosa', isNative= False, image_name= 'Common_Sorrel_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '0.6 meters, juicy').save()
Leaves(plant=plant, shapes= 'AR', desc= 'upper leaves often red, 7-15cm long', image_name= 'Common_Sorrel_Leaves.jpg').save()
Flowers(plant= plant, colors= 'Red-Green, Purple', desc= 'Reddish-green to purplish spikes of flowers', image_name= 'Common_Sorrel_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Common Toadflax 23
name = 'Common Toadflax'
Plants(name= name, latin_name= 'Linaria vulgaris', isNative= False, image_name= 'Common_Toadflax_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= 'Up to 1 meter, Tough at the base, branching').save()
Leaves(plant=plant, shapes= 'LI', desc= 'Narrow, slightly pointed at both ends, crowded along the stem').save()
Flowers(plant= plant, colors= 'Yellow', desc= 'has orange center, two-lipped, 2-4cm long, fuzzy throated', image_name= 'Common_Toadflax_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Common Yarrow 24
name = 'Common Yarrow'
Plants(name= name, latin_name= 'Achillea millefolium', image_name= 'Common_Yarrow_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= 'Up to 1 meter, Fine white hairs').save()
Leaves(plant=plant, shapes= 'LA', desc= 'finely divided, 3-15cm long and 2.5cm wide', image_name= 'Common_Yarrow_Leaves.jpg').save()
Flowers(plant= plant, colors= 'White, Pink', desc= 'in a flat-topped or rounded cluster at the end of branches', image_name= 'Common_Yarrow_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Cow Parsnip 25
name = 'Cow Parsnip'
Plants(name= name, latin_name= 'Heracleum maximum', image_name= 'Cow_Parsnip_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= 'Over 2 meters, Brown-green, round').save()
Leaves(plant=plant, shapes= 'TL', desc= 'Very large', image_name= 'Cow_Parsnip_Leaves.jpg').save()
Flowers(plant= plant, colors= 'White', desc= 'small, in umbels 20cm across', image_name= 'Cow_Parsnip_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Cow Vetch 26
name = 'Cow Vetch'
Plants(name= name, latin_name= 'Vicia cracca', isNative= False, image_name= 'Cow_Vetch_Flowers.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '1-2 meters, Green at base, brown at tips').save()
Leaves(plant=plant, shapes= 'OB', desc= 'Small, pinnate, long, broad, 5-11 pairs of leaflets', image_name= 'Cow_Vetch_Leaves.jpg').save()
Flowers(plant= plant, colors= 'Purple-Blue', desc= 'in groups of 10-40 at the end of the stem, 8-13mm', image_name= 'Cow_Vetch_Flowers.jpg').save()
Berries(plant= plant,desc= 'In pods similar to peas').save()
print(plant.name + ' Complete!!!')

#Creeping Bentgrass 27
name = 'Creeping Bentgrass'
Plants(name= name, latin_name= 'Agrostis stolonifera', isNative= False, image_name= 'Creeping_Bentgrass_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= 'Grass').save()
Leaves(plant=plant, shapes= 'LI', desc= 'Smooth, narrow, 1cm wide and 1-15cm long').save()
Berries(plant= plant,desc= 'Occurs in a plume 2-20cm long and 1-12cm wide''Creeping_Bentgrass_Seedhead.jpg').save()
print(plant.name + ' Complete!!!')

#Curly Dock 28
name = 'Curly Dock'
Plants(name= name, latin_name= 'Rumex crispus', isNative= False, image_name= 'Curly_Dock_Green_Flowers.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= 'o.6-1.2 meters, Green').save()
Leaves(plant=plant, shapes= 'OL', desc= 'Long with curly edges, coarse texture', image_name= 'Curly_Dock_Leaves.jpg').save()
Flowers(plant= plant, colors= 'Green, Red', desc= 'turns deep red with maturity, in clusters at the end of a long stem', image_name= 'Curly_Dock_Red_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Dame's Rocket 29
name = 'Dame\'s Rocket'
Plants(name= name, latin_name= 'Hesperis matronalis', isNative= False, image_name= 'Dames_Rocket_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '1 meter or more, Multiple, upright, hairy').save()
Leaves(plant=plant, shapes= 'LA', desc= 'Toothed, long').save()
Flowers(plant= plant, colors= 'Purple, White, Pink', desc= 'four-petaled forming a mock tube at the base', image_name= 'Dames_Rocket_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Dark Green Bullrush 30
name = 'Dark Green Bulrush'
Plants(name= name, latin_name= 'Scirpus atrovirens', isNative= False, image_name= 'Dark_Green_Bulrush_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '0.8-1.2 meters, Unbranched, more or less erect, green').save()
Leaves(plant=plant, shapes= 'LI', desc= 'Yellow to dark green, up to 8, alternate, furrowed, flat, rough-edged, 3.5cm long and 2cm wide').save()
Berries(plant= plant, colors= 'Brown',desc= 'spiky clusters', image_name= 'Dark_Green_Bulrush_Seedheads.jpg').save()
print(plant.name + ' Complete!!!')

#Ditch Stonecrop 31
name = 'Ditch Stonecrop'
Plants(name= name, latin_name= 'Penthorum sedoides', image_name= 'Ditch_Stonecrop_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '0.3-0.6 meters, Light reddish-green').save()
Leaves(plant=plant, shapes= 'OL', desc= 'Alternate, 10cm long and 2cm wide, elliptic or ovate, serrated, with a midvein', image_name= 'Ditch_Stonecrop_Leaves.jpg').save()
Flowers(plant= plant, colors= 'Green', desc= 'on  upper stems, in groups 2-7cm across').save()
print(plant.name + ' Complete!!!')

#English Violet 32
name = 'English Violet'
Plants(name= name, latin_name= 'Viola odorata', isNative= False, image_name= 'English_Violet_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '0.2-0.3 meters, leafless').save()
Leaves(plant=plant, shapes= 'HT').save()
Flowers(plant= plant, colors= 'Purple', desc= 'at the end of a stalk, two petals at the top and three at the bottom', image_name= 'English_Violet_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Field Bindweed 33
name = 'Field Bindweed'
Plants(name= name, latin_name= 'Convolvulus arvensis', isNative= False, image_name= 'Field_Bindweed_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= 'Vine, hairless').save()
Leaves(plant=plant, shapes= 'HT', desc= 'Alternate, triangular or heart shaped, 2-6cm long', image_name= 'Field_Bindweed_Leaves_Stem.jpg').save()
Flowers(plant= plant, colors= 'White, Pink', desc= 'trumpet-shaped, 1-2.5cm').save()
print(plant.name + ' Complete!!!')

#Forget-Me-Not 34
name = 'Forget-Me-Not'
Plants(name= name, latin_name= 'Myosotis scorpioides', isNative= False, image_name= 'Forget_Me_Not_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= 'Up to 0.7 meters, yellow-green, round').save()
Leaves(plant=plant, shapes= 'OB, LI', desc= 'fuzzy on both sides').save()
Flowers(plant= plant, colors= 'Blue', desc= 'Pink buds, blue flowers with yellow centers and white honey guides, 8-12mm', image_name= 'Forget_Me_Not_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Foxtail 35
name = 'Foxtail'
Plants(name= name, latin_name= 'Setaria glauca', isNative= False, image_name= 'Foxtail_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= 'Up to 1 meter, Grass').save()
Leaves(plant=plant, shapes= 'LI', desc= 'Smooth underside but hairs on upper at base, 30cm long and 4-10mm wide').save()
Berries(plant= plant, colors= 'Yellow',desc= 'Yellow bristles, spikelets 3mm long, yellow seeds 2-3mm long', image_name= 'Foxtail_Seedhead.jpg').save()
print(plant.name + ' Complete!!!')

#Garden Valerian 36
name = 'Garden Valerian'
Plants(name= name, latin_name= 'Valeriana officinalis', isNative= False, image_name= 'Garden_Valerian_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= 'Up to 1.5 meters, Green, round').save()
Leaves(plant=plant, shapes= 'CP', desc= 'Opposite').save()
Flowers(plant= plant, colors= 'White, Pink', desc= 'scented, in clusters', image_name= 'Garden_Valerian_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Garlic Mustard 37
name = 'Garlic Mustard'
Plants(name= name, latin_name= 'Alliara petiolata', isNative= False, image_name= 'Garlic_Mustard_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '0.6-1meter, Green, upright').save()
Leaves(plant=plant, shapes= 'HT', desc= 'Kidney shaped, scalloped edges').save()
Flowers(plant= plant, colors= 'White', desc= 'small, four-petaled, clustered at stem ends', image_name= 'Garlic_Mustard_Flowers.jpg').save()
Berries(plant= plant,desc= 'Long, skinny pods', image_name= 'Garlic_Mustard_Seeds.jpg').save()
print(plant.name + ' Complete!!!')

#Giant St John's Wort 38
name = 'Giant St John\'s Wort'
Plants(name= name, latin_name= 'Hypericum ascyron', isNative= False, image_name= 'Giant_St_Johns_Wort_Plants.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '1-1.5 meters, Erect, branched in the top 1/3 of the plant, light green, 4-angled').save()
Leaves(plant=plant, shapes= 'LA, OL', desc= 'Lanceolate-ovate, opposite, smooth edges, 10cm long and 4cm wide', image_name= 'Giant_St_Johns_Wort_Leaves.jpg').save()
Flowers(plant= plant, colors= 'Yellow', desc= 'groups of 1-5 flowers 5cm across', image_name= 'Giant_St_Johns_Wort_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Gloden Button 39
name = 'Gloden Button'
Plants(name= name, latin_name= 'Tanacetum vulgare', isNative= False, image_name= 'Golden_Buttons_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '1-2 meters').save()
Leaves(plant=plant, shapes= 'CP', desc= 'fernlike, 15cm').save()
Flowers(plant= plant, colors= 'Yellow', desc= 'round', image_name= 'Golden_Buttons_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Goldenrod 40
name = 'Goldenrod'
Plants(name= name, latin_name= 'Solidago canadensis', image_name= 'Goldenrod_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '0.5-1.5 meters, Upright, branched').save()
Leaves(plant=plant, shapes= 'OL', desc= 'Narrow, alternate, larger at base of stem, 3-15cm long', image_name= 'Goldenrod_Leaves.jpg').save()
Flowers(plant= plant, colors= 'Yellow', desc= 'at top of branches in groups of about 14', image_name= 'Goldenrod_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Great Willowherb 41
name = 'Great Willowherb'
Plants(name= name, latin_name= 'Epilobium hirsutum', isNative= False, image_name= 'Great_Willowherb_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '1-1.5 meters, Hairy').save()
Leaves(plant=plant, shapes= 'LA', desc= 'Long, narrow').save()
Flowers(plant= plant, colors= 'Purple', desc= 'small, 2-5cm', image_name= 'Great_Willowherb_Flower.jpg').save()
print(plant.name + ' Complete!!!')

#Green Bristle Grass 42
name = 'Green Bristle Grass'
Plants(name= name, latin_name= 'Setaria viridis', isNative= False, image_name= 'Green_Bristle_Grass_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= 'Up to 1 meter, Grass').save()
Leaves(plant=plant, shapes= 'LI', desc= '40cm long and 2.5cm wide').save()
Berries(plant= plant, desc= 'Spikelets with bristles at the end of the stems', image_name= 'Green_Bristle_Grass_Seedhead.jpg').save()
print(plant.name + ' Complete!!!')

#Ground Ivy 43
name = 'Ground Ivy'
Plants(name= name, latin_name= 'Glechoma hederacea', isNative= False, image_name= 'Ground_Ivy_Flowers.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= 'Vine, Square').save()
Leaves(plant=plant, shapes= 'HT', desc= 'Rounded, kidney to heart shaped, curving into stalk', image_name= 'Ground_Ivy_Leaves.jpg').save()
Flowers(plant= plant, colors= 'Purple, Blue', desc= 'in clusters of 2-3, growing from stem', image_name= 'Ground_Ivy_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Horsetail 44
name = 'Horsetail'
Plants(name= name, latin_name= 'Equisetum arvense', image_name= 'Horsetail_Stems.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '0.3 meters, Erect leafless cone-bearing stem, or vegetative stem with whorls of leafless branches at the nodes').save()
Leaves(plant= plant, image_name= 'Horsetail_Leaves.jpg').save()
Berries(plant= plant,desc= 'Cones', image_name= 'Horsetail_Cones.jpg').save()
print(plant.name + ' Complete!!!')

# Italian Ryegrass 45
name = 'Italian Ryegrass'
Plants(name= name, latin_name= 'Lolium multiflorum', isNative= False, image_name= 'Italian_Ryegrass_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '1 meter, Grass').save()
Leaves(plant=plant, shapes= 'LI', desc= 'Narrowing to tip, 6-20cm long').save()
Berries(plant= plant, desc= '10-40cm spike with alternating 1.5-2.5cm spikelets', image_name= 'Italian_Ryegrass_Seedhead.jpg').save()
print(plant.name + ' Complete!!!')

#Jerusalem Artichokes 46
name = 'Jerusalem Artichokes'
Plants(name= name, latin_name= 'Helianthus tuberosus', isNative= False, image_name= 'Jerusalem_Artichoke_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '1-3 meters, Coarse with rough hairs').save()
Leaves(plant=plant, shapes= 'OL, HT', desc= 'rough on top, gray hairs underneath, opposite at bottom and alternate at top of stem, 10-25cm long and 3-12cm wide').save()
Flowers(plant= plant, colors= 'Yellow', desc= '1-5 flowers at the end of a stem, about 5cm in diameter', image_name= 'Jerusalem_Artichoke_Flower.jpg').save()
print(plant.name + ' Complete!!!')

#Joe Pye Weed 47
name = 'Joe Pye Weed'
Plants(name= name, latin_name= 'Eutrochium purpureum, Eutrochium maculatum', image_name= 'Joe_Pye_Weed_Plants.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '1-2.5 meters, Brown').save()
Leaves(plant=plant, shapes= 'LA', desc= 'Long, serrated, in groups of 5-6').save()
Flowers(plant= plant, colors= 'Pink, Purple', desc= 'small, vanilla scented, clusters at top of stem', image_name= 'Joe_Pye_Weed_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Johnson Grass 48
name = 'Johnson Grass'
Plants(name= name, latin_name= 'Sorghum halepense', isNative= False, image_name= 'Johnson_Grass_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '2 meters, Grass').save()
Leaves(plant=plant, shapes= 'LI', desc= 'Smooth on both sides, white vein in the middle, 4-18cm long').save()
Berries(plant= plant, colors= 'Purple',desc= 'branching cluster, 15-50cm', image_name= 'Johnson_Grass_Seedhead.jpg').save()
print(plant.name + ' Complete!!!')

#Ladybell 49
name = 'Ladybell'
Plants(name= name, latin_name= 'Adenophora liliifolia', isNative= False, image_name= 'Ladybell_Plants.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '0.6-0.8 meters, Green, round').save()
Leaves(plant=plant, shapes= 'DL', desc= 'Alternate, serated').save()
Flowers(plant= plant, colors= 'Blue', desc= 'bell-shaped, hanging, in spikes at the end of the stem', image_name= 'Ladybell_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Lilac 50
name = 'Lilac'
Plants(name= name, latin_name= 'Syringa vulgaris', isNative= False, image_name= 'Lilac_Flowers.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '6-7 meters, Grey to grey-brown bark').save()
Leaves(plant=plant, shapes= 'DL', desc= 'Opposite, shiny upper surface', image_name= 'Lilac_Leaves.jpg').save()
Flowers(plant= plant, colors= 'White, Purple, Pink, Blue', desc= ' in clusters', image_name= 'Lilac_Flowers.jpg').save()
Berries(plant= plant, desc= 'Three-lobed seed capsule').save()
print(plant.name + ' Complete!!!')

#Lily 51
name = 'Lily'
Plants(name= name, latin_name= 'Lilium candidum', isNative= False, image_name= 'Lily_Plants.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '1.2 meters, Leafy').save()
Leaves(plant=plant, shapes= 'LA', desc= 'In clusters around the stem').save()
Flowers(plant= plant, colors= 'White', desc= 'White with yellow throat', image_name= 'Lily_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Meadow Grass 52
name = 'Meadow Grass'
Plants(name= name, latin_name= 'Poa annua', isNative= False, image_name= 'Meadow_Grass_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '0.2-0.3 meters, Grass, slightly flattened').save()
Leaves(plant=plant, shapes= 'LI', desc= 'Vivid green, short and blunt at tips, in leaf year round').save()
Berries(plant= plant, desc= 'Panicle 5-7.5cm long with 1-2cm spikelets', image_name= 'Meadow_Grass_Seedhead.jpg').save()
print(plant.name + ' Complete!!!')

#Meadowsweet 53
name = 'Meadowsweet'
Plants(name= name, latin_name= 'Filipendula ulmaria', isNative= False, image_name= 'Meadowsweet_Plants.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '1-2 meters, Brown, woody').save()
Leaves(plant=plant, shapes= 'LA', desc= 'Toothed, in pairs, 10-20cm long').save()
Flowers(plant= plant, colors= 'White', desc= 'puffy, large, in clusters of 20 at top of plant', image_name= 'Meadowsweet_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Milkweed 54
name = 'Milkweed'
Plants(name= name, latin_name= 'Asclepias syriaca', image_name= 'Milkweed_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '0.5-1.5 meters, Green, round').save()
Leaves(plant=plant, shapes= 'OL', desc= 'opposite, 7-20cm long').save()
Flowers(plant= plant, colors= 'Purple, Pink', desc= 'globe shaped, in clusters', image_name= 'Milkweed_Flowers.jpg').save()
Berries(plant= plant, colors= 'Green',desc= 'oval pods').save()
print(plant.name + ' Complete!!!')

#Morning Glory 55
name = 'Morning Glory'
Plants(name= name, latin_name= 'Convolvulaceae family', isNative= False, image_name= 'Morning_Glory_Flowers.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= 'Vine, green, round').save()
Leaves(plant=plant, shapes= 'HT, LB', desc= 'Heart shaped with lobed bases', image_name= 'Morning_Glory_Leaves.jpg').save()
Flowers(plant= plant, colors= 'Pink, White', desc= '1-2.5cm', image_name= 'Morning_Glory_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Mullein 56
name = 'Mullein'
Plants(name= name, latin_name= 'Verbascum thapsus', isNative= False, image_name= 'Mullein_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '0.5-3 meters, tall').save()
Leaves(plant=plant, shapes= 'LA', desc= 'Dense rosette at the ground, spirally arranged, often hairy, alternate up the stem', image_name= 'Mullein_Leaves.jpg').save()
Flowers(plant= plant, colors= 'Yellow, Orange, Red-Brown, Purple, Blue, White', desc= 'in spike at the top of the stem', image_name= 'Mullein_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Netted Chain Fern 57
name = 'Netted Chain Fern'
Plants(name= name, latin_name= 'Woodwardia areolata', image_name= 'Netted_Chain_Fern_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= 'Up to 0.6 meters, green').save()
Leaves(plant=plant, shapes= 'LA', desc= 'Lance-shaped pinnae with small teeth, 50-70cm long', image_name= 'Netted_Chain_Fern_Leaves.jpg').save()
print(plant.name + ' Complete!!!')

#Oriental Bittersweet 58
name = 'Oriental Bittersweet'
Plants(name= name, latin_name= 'Celastrus orbiculatus', isNative= False, image_name= 'Oriental_Bittersweet_Berries.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= 'Vine, Silver to reddish brown, woody').save()
Leaves(plant=plant, shapes= 'OL', desc= 'Rounded to opovate, alternate, toothed margins, 2-12cm long', image_name= 'Oriental_Bittersweet_Flowers_Leaves.jpg').save()
Flowers(plant= plant, colors= 'Green', desc= 'small', image_name= 'Oriental_Bittersweet_Flowers_Leaves.jpg').save()
Berries(plant= plant, colors= 'Red, Yellow',desc= 'Red seeds in yellow pods', image_name= 'Oriental_Bittersweet_Berries.jpg').save()
print(plant.name + ' Complete!!!')

#Oxeye Daisy 59
name = 'Oxeye Daisy'
Plants(name= name, latin_name= 'Leucanthemum vulgare', isNative= False, image_name= 'Oxeye_Daisy_Plants.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '0.3-1 meter, Smooth, hairless').save()
Leaves(plant=plant, shapes= 'LB', desc= 'Smooth, hairless, rounded lobes on margins, 5-12cm long at base of stem and smaller up stem', image_name= 'Oxeye_Daisy_Leaves.jpg').save()
Flowers(plant= plant, colors= 'White', desc= 'yellow center, 20-30 petals, 2-5cm diameter, single flower on end of stem', image_name= 'Oxeye_Daisy_Flower.jpg').save()
print(plant.name + ' Complete!!!')

#Pale Swallow Wort 60
name = 'Pale Swallow Wort'
Plants(name= name, latin_name= 'Vincetoxicum rossicum', isNative= False, image_name= 'Pale_Swallow_Wort_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '0.6-2 meters').save()
Leaves(plant=plant, shapes= 'OL', desc= 'Larger closer to stem, ellipse or oval, smooth margin, veins underneath, opposite', image_name= 'Pale_Swallow_Wort_Leaves.jpg').save()
Flowers(plant= plant, colors= 'Pink', desc= 'star shaped, at top of plant', image_name= 'Pale_Swallow_Wort_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Peoney 61
name = 'Peoney'
Plants(name= name, latin_name= 'Paeonia x suffruticosa', isNative= False, image_name= 'Peony_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '0.25-1 meter').save()
Leaves(plant=plant, shapes= 'CP', desc= 'deeply lobed', image_name= 'Peony_Leaves.jpg').save()
Flowers(plant= plant, colors= 'Red, Pink, White, Yellow', desc= 'single or double bloom', image_name= 'Peony_Flower.jpg').save()
print(plant.name + ' Complete!!!')

#Philadelphia Daisy 62
name = 'Philadelphia Daisy'
Plants(name= name, latin_name= 'Erigeron philadelphicus', image_name= 'Philadelphia_Daisy_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= 'Hairy').save()
Leaves(plant=plant, shapes= 'HT', desc= 'alternate, simple').save()
Flowers(plant= plant, colors= 'Pink, White', desc= 'yellow centers, 2.5cm, up to 400 petals', image_name= 'Philadelphia_Daisy_Flower.jpg').save()
print(plant.name + ' Complete!!!')

#Phragmites 63
name = 'Phragmites'
Plants(name= name, latin_name= 'Phragmites australis', isNative= False, image_name= 'Phragmites_Leaves.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '2-4 meters, grass, hollow').save()
Leaves(plant=plant, shapes= '', desc= 'On same side of stem, flat, 20-60cm and 2.5cm wide', image_name= 'Phragmites_Leaves.jpg').save()
Berries(plant= plant, colors= 'Purple, Gold', desc= 'Purple to gold plumes 15-40cm', image_name= 'Phragmites_Seedheads.jpg').save()
print(plant.name + ' Complete!!!')

#Purple Loosestrife 64
name = 'Purple Loosestrife'
Plants(name= name, latin_name= 'Lythrum salicara', isNative= False, image_name= 'Purple_Loosestrife_Plants.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '1-2 meters, Reddish-purple, erect').save()
Leaves(plant=plant, shapes= 'TL', desc= 'Opposite pairs or threes, smooth edged, 3-10cm', image_name= 'Purple_Loosestrife_Leaves.jpg').save()
Flowers(plant= plant, colors= 'Red-Purple', desc= 'Reddish purple, clustered in spikes at top of stem, 10-20mm', image_name= 'Purple_Loosestrife_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Purpletop Tridens 65
name = 'Purpletop Tridens'
Plants(name= name, latin_name= 'Tridens flavus', isNative= False, image_name= 'Purpletop_Tridens_Plants.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '1-1.5 meters, grass').save()
Leaves(plant=plant, shapes= 'LI', desc= 'Alternate, shallowly grooved or flat, rough to the touch, 45cm long and 0.1cm wide', image_name= 'Purpletop_Tridens_Leaves.jpg').save()
Berries(plant= plant, colors= 'Brown, Red-Purple', desc= 'airy, pyramidal outline, 2mm long', image_name= 'Purpletop_Tridens_Seedhead.jpg').save()
print(plant.name + ' Complete!!!')

#Queen Anne's Lace 66
name = 'Queen Anne\'s Lace'
Plants(name= name, latin_name= 'Daucus carota', isNative= False, image_name= 'Queen_Annes_Lace_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= 'Up to 1 meter, Green').save()
Leaves(plant=plant, shapes= 'LB', desc= 'Alternate, triangular, 15cm long', image_name= 'Queen_Annes_Lace_Leaves.jpg').save()
Flowers(plant= plant, colors= 'White', desc= 'flat to umbrella shaped clusters with a single dark flower in the center', image_name= 'Queen_Annes_Lace_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Raspberry 67
name = 'Raspberry'
Plants(name= name, latin_name= 'Rubus strigosus', image_name= 'Raspberry_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '0.5-2 meters, Red or green with prickles').save()
Leaves(plant=plant, shapes= 'CP', desc= 'Alternate, 3-7 leaflets', image_name= 'Raspberry_Berries_Leaves.jpg').save()
Flowers(plant= plant, colors= 'White', desc= 'small').save()
Berries(plant= plant, colors= 'Red',desc= 'edible berries, 1-1.2cm', image_name= 'Raspberry_Berries_Leaves.jpg').save()
print(plant.name + ' Complete!!!')

#Redstem Filaree 68
name = 'Redstem Filaree'
Plants(name= name, latin_name= 'Erodium cicutarium', isNative= False, image_name= 'Redstem_Filaree_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '0.1-0.5 meters, Reddish, low, hairy').save()
Leaves(plant=plant, shapes= 'LB', desc= 'Deeply cut, nearly to midvein').save()
Flowers(plant= plant, colors= 'Pink, Purple', desc= 'clusters of 2-8', image_name= 'Redstem_Filaree_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Reed Canary Grass 69 (Nice)
name = 'Reed Canary Grass'
Plants(name= name, latin_name= 'Phalaris arundinacea', image_name= 'Reed_Canary_Grass_Plants.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '1.5 meters, grass').save()
Leaves(plant=plant, shapes= 'LI', desc= 'Green, attached to stem by a collar, 10-35cm long', image_name= 'Reed_Canary_Grass_Leaves.jpg').save()
Berries(plant= plant, colors= 'Light-Green', desc= 'Light green, branching cluster, 7-25cm', image_name= 'Reed_Canary_Grass_Seedhead.jpg').save()
print(plant.name + ' Complete!!!')

#Rhubarb 70
name = 'Rhubarb'
Plants(name= name, latin_name= 'Rheum x hybridum', isNative= False, image_name= 'Rhubarb_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '1 meter, Deep red, pink, or green').save()
Leaves(plant=plant, shapes= 'HT', desc= 'large, dark', image_name= 'Rhubarb_Leaves.jpg').save()
print(plant.name + ' Complete!!!')

#Ribwort Plantain 71
name = 'Ribwort Plantain'
Plants(name= name, latin_name= 'Plantago lanceolata', isNative= False, image_name= 'Ribwort_Plantain_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '0.1-0.4 meters, Leafless, silky, hairy').save()
Leaves(plant=plant, shapes= 'LA', desc= 'toothed, 3-5 parallel veins, 2-30cm long and 0.5-3.5cm wide', image_name= 'Ribwort_Plantain_Leaves.jpg').save()
Flowers(plant= plant, colors= 'White', desc= 'at the end of a tall stem, blooming from a dark brown spike', image_name= 'Ribwort_Plantain_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Round Fruited Rush 72
name = 'Round Fruited Rush'
Plants(name= name, latin_name= 'Juncus compressus', isNative= False, image_name= 'Round_Fruited_Rush_Plants.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '0.8 meters, Grass').save()
Leaves(plant=plant, shapes= 'LI', desc= 'Flat, narrow, 5-35cm long').save()
Berries(plant= plant, desc= 'Capsules holding seeds clustered at top of stem', image_name= 'Round_Fruited_Rush_Seedhead.jpg').save()
print(plant.name + ' Complete!!!')

#Smooth Bedstraw 73
name = 'Smooth Bedstraw'
Plants(name= name, latin_name= 'Galium mollugo', isNative= False, image_name= 'Smooth_Bedstraw_Leaves.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= 'Up to 1 meter, upright initially but spread over time, wiry, angled, branched').save()
Leaves(plant=plant, shapes= 'LI', desc= 'Bright green, linear, whorled, 1-2.5cm long', image_name= 'Smooth_Bedstraw_Leaves.jpg').save()
Flowers(plant= plant, colors= 'White', desc= 'clustered, tiny', image_name= 'Smooth_Bedstraw_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Smooth Brome 74
name = 'Smooth Brome'
Plants(name= name, latin_name= 'Bromus inermus', isNative= False, image_name= 'Smooth_Brome_Stem.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= 'Up to 1.5 meters, Grass, very thin').save()
Leaves(plant=plant, shapes= 'LI', desc= 'Flat with a raised midrib underneath, 20-35cm long and 1cm wide', image_name= 'Smooth_Brome_Leaves.jpg').save()
Berries(plant= plant, colors= 'Brown', desc= 'compact, branched with spikelets', image_name= 'Smooth_Brome_Seedhead.jpg').save()
print(plant.name + ' Complete!!!')

#Soybean 75
name = 'Soybean'
Plants(name= name, latin_name= 'Glycine max', isNative= False, image_name= 'Soybean_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '0.5-1.2 meters, woody, not corn').save()
Leaves(plant=plant, shapes= 'TL, OL, LA', desc= 'alternate, 2-20cm long', image_name= 'Soybean_Leaves.jpg').save()
Flowers(plant= plant, colors= 'White, Purple', desc= 'small').save()
Berries(plant= plant, desc= 'curved pods 2-15cm long', image_name= 'Soybean_Seedpods.jpg').save()
print(plant.name + ' Complete!!!')

#Spotted Knapweed 76
name = 'Spotted Knapweed'
Plants(name= name, latin_name= 'Centaurea stoebe', isNative= False, image_name= 'Spotted_Knapweed_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '0.6-1 meter, erect, slender, wiry, branched').save()
Leaves(plant=plant, shapes= 'LB', desc= 'Gray-green, alternate, pinnate with many lobes, rough bristles on edges, 15cm long', image_name= 'Spotted_Knapweed_Leaves.jpg').save()
Flowers(plant= plant, colors= 'Pink, Purple', desc= 'extend out of small pineapple shape, similar to thistle', image_name= 'Spotted_Knapweed_Flower.jpg').save()
print(plant.name + ' Complete!!!')

#Spotted Touch-Me-Not 77
name = 'Spotted Touch-Me-Not'
Plants(name= name, latin_name= 'Impatiens capensis', image_name= 'Spotted_Touch_Me_Not_Plants.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '1-1.5 meters, branched').save()
Leaves(plant=plant, shapes= 'OL', desc= 'Egg shaped, wide teeth, 10cm long', image_name= 'Spotted_Touch_Me_Not_Leaves.jpg').save()
Flowers(plant= plant, colors= 'Orange', desc= 'small, bell shaped, in groups of 1-4', image_name= 'Spotted_Touch_Me_Not_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Softstem Bulrush 78
name = 'Softstem Bulrush'
Plants(name= name, latin_name= 'Schoenoplectus tabernaemontani', image_name= 'Softstem_Bulrush_Plants.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= 'Up to 3 meters, Grass').save()
Leaves(plant=plant, shapes= 'LI', desc= 'small at base').save()
Berries(plant= plant, colors= 'Dark Brown',desc= 'drooping cluster at stem tip', image_name= 'Softstem_Bulrush_Seedheads.jpg').save()
print(plant.name + ' Complete!!!')

#Soft Rush 79
name = 'Soft Rush'
Plants(name= name, latin_name= 'Juncus effusus', image_name= 'Soft_Rush_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= 'Up t 1 meter, grass').save()
Leaves(plant=plant, shapes= 'LI', desc= 'Long, brown, at base, narrow, 15cm long').save()
Berries(plant= plant, colors= 'Yellow, Brown',desc= 'on one side of stem, at top of plant', image_name= 'Soft_Rush_Seedheads.jpg').save()
print(plant.name + ' Complete!!!')

#Stinging Nettle 80
name = 'Stinging Nettle'
Plants(name= name, latin_name= 'Urtica dioica', image_name= 'Stinging_Nettle_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '1-2 meters, Green, erect, wiry, SKIN IRRITANT').save()
Leaves(plant=plant, shapes= 'DL', desc= 'Stinging hairs on underside, opposite, deeply toothed, 3-15cm long', image_name= 'Stinging_Nettle_Leaves.jpg').save()
Flowers(plant= plant, colors= 'Green, Brown', desc= 'growing between leaves on stem', image_name= 'Stinging_Nettle_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Swamp Loosestrife 81
name = 'Swamp Loosestrife'
Plants(name= name, latin_name= 'Decodon verticillatus', image_name= 'Swamp_Loosestrife_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '1 meter, Pinkish, woody at base').save()
Leaves(plant=plant, shapes= 'LA', desc= 'Hairy, opposite, 20cm long').save()
Flowers(plant= plant, colors= 'Purple', desc= 'small, at base of leaves', image_name= 'Swamp_Loosestrife_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Tall Fescue 82
name = 'Tall Fescue'
Plants(name= name, latin_name= 'Festuca arundinacea', isNative= False, image_name= 'Tall_Fescue_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '1.5 meters, grass').save()
Leaves(plant=plant, shapes= 'LI', desc= 'Attached to stem by white collar, 10-60cm long').save()
Berries(plant= plant, colors= 'Green',desc= 'in groups of 3-8, on spikelet at top of plant, 1-1.8cm', image_name= 'Tall_Fescue_Seedhead.jpg').save()
print(plant.name + ' Complete!!!')

#Tatarian Honeysuckle 83
name = 'Tatarian Honeysuckle'
Plants(name= name, latin_name= 'Lonicera tatarica', isNative= False, image_name= 'Tatarian_Honeysuckle_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '3-4 meters, Light brown-tan, scaly bark').save()
Leaves(plant=plant, shapes= 'DL', desc= 'Opposite, egg shaped, hairy', image_name= 'Tatarian_Honeysuckle_Leaves_Berries.jpg').save()
Flowers(plant= plant, image_name= 'Tatarian_Honeysuckle_Flowers.jpg').save()
Berries(plant= plant, colors= 'Red',desc= 'berries, 6mm', image_name= 'Tatarian_Honeysuckle_Leaves_Berries.jpg').save()
print(plant.name + ' Complete!!!')

#Timothy 84
name = 'Timothy'
Plants(name= name, latin_name= 'Phleum pratense', isNative= False, image_name= 'Timothy_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= 'up to 1 meter, grass').save()
Leaves(plant=plant, shapes= 'LA', desc= 'Rolled at bud, sheath fused around stem, hairless, 43cm long and 1.5cm wide', image_name= 'Timothy_Leaves.jpg').save()
Berries(plant= plant, colors= 'Green',desc= 'dense spikelets', image_name= 'Timothy_Seedheads.jpg').save()
print(plant.name + ' Complete!!!')

#Velvet Grass 85
name = 'Velvet Grass'
Plants(name= name, latin_name= 'Holcus lanatus', isNative= False, image_name= 'Velvet_Grass_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '1 meter, Grass').save()
Leaves(plant=plant, shapes= 'LI', desc= 'Only a few, covered in soft hairs, 4-20cm long and narrow', image_name= 'Velvet_Grass_Leaves.jpg').save()
Berries(plant= plant, colors= 'Purple',desc= 'at top of plant', image_name= 'Velvet_Grass_Seedheads.jpg').save()
print(plant.name + ' Complete!!!')

#Virginia Creeper 86
name = 'Virginia Creeper'
Plants(name= name, latin_name= 'Parthenocissus quinquefolia', image_name= 'Virginia_Creeper_Green_Berries.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= 'Vine, Green or woody').save()
Leaves(plant=plant, shapes= 'CP', desc= 'in groups of 5, toothed margins, alternate, 3-20cm across', image_name= 'Virginia_Creeper_Leaves.jpg').save()
Berries(plant= plant, colors= 'Green, Purple',desc= 'Greenish berries, small, purple-black when mature', image_name= 'Virginia_Creeper_Purple_Berries.jpg').save()
print(plant.name + ' Complete!!!')

#Wartweed 87
name = 'Wartweed'
Plants(name= name, latin_name= 'Euphorbia peplus', isNative= False, image_name= 'Wartweed_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= 'Up to 0.3 meters, smooth, hairless').save()
Leaves(plant=plant, shapes= 'OL', desc= 'Oval-acute, smooth margin, 1-3cm long', image_name= 'Wartweed_Leaves_Flowers.jpg').save()
Flowers(plant= plant, colors= 'Green', desc= 'small', image_name= 'Wartweed_Leaves_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#White Sweet Clover 88
name = 'White Sweet Clover'
Plants(name= name, latin_name= 'Melilotus alba', isNative= False, image_name= 'White_Sweet_Clover_Plants.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= 'Up to 2.5 meters, light green, branching').save()
Leaves(plant=plant, shapes= 'OL', desc= 'alternate, trifoliate', image_name= 'White_Sweet_Clover_Leaves.jpg').save()
Flowers(plant= plant, colors= 'White', desc= 'clustered on spikes, from top of plant and where leaves meet stem', image_name= 'White_Sweet_Clover_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#White Turtlehead 89
name = 'White Turtlehead'
Plants(name= name, latin_name= 'Chelone glabra', image_name= 'White_Turtlehead_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= 'Up to 1 meter, Green, smooth').save()
Leaves(plant=plant, shapes= 'LA', desc= 'Narrow, spiked, 20cm long', image_name= 'White_Turtlehead_Leaves.jpg').save()
Flowers(plant= plant, colors= 'White', desc= 'small, shape suggests a turtle head', image_name= 'White_Turtlehead_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Wild Grape 90
name = 'Wild Grape'
Plants(name= name, latin_name= 'Vitis spp.', image_name= 'Wild_Grape_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= 'Vine, woody').save()
Leaves(plant=plant, shapes= 'HT', desc= 'alternate, long tips', image_name= 'Wild_Grape_Leaves_Grapes.jpg').save()
Flowers(plant= plant, colors= 'White', desc= 'small').save()
Berries(plant= plant, colors= 'Purple',desc= 'grapes', image_name= 'Wild_Grape_Leaves_Grapes.jpg').save()
print(plant.name + ' Complete!!!')

#Wild Parsnip 91
name = 'Wild Parsnip'
Plants(name= name, latin_name= 'Pastinaca sativa', isNative= False, image_name= 'Wild_Parsnip_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '0.3-1.5 meters, hairy lower, bare upper, milky sap if cut. DO NOT TOUCH ANY PART OF THIS PLANT').save()
Leaves(plant=plant, shapes= 'OL', desc= 'Broad, hairless, ovate, paired', image_name= 'Wild_Parsnip_Leaves.jpg').save()
Flowers(plant= plant, colors= 'Yellow', desc= 'small, clustered in an umbrella shape', image_name= 'Wild_Parsnip_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Wild Strawberry 92
name = 'Wild Strawberry'
Plants(name= name, latin_name= 'Fragaria vesca', image_name= 'Wild_Strawberry_Flowers_Berries.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= 'Up to 0.1 meters, Hairy').save()
Leaves(plant=plant, shapes= 'TL, OL', desc= 'Toothed margins, smooth, trifoliate', image_name= 'Wild_Strawberry_Leaves.jpg').save()
Flowers(plant= plant, colors= 'White', image_name= 'Wild_Strawberry_Flowers_Berries.jpg').save()
Berries(plant= plant, colors= 'Red',desc= 'Strawberries', image_name= 'Wild_Strawberry_Flowers_Berries.jpg').save()
print(plant.name + ' Complete!!!')

#Winterberry 93
name = 'Winterberry'
Plants(name= name, latin_name= 'Ilex verticillata', image_name= 'Winterberry_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '1-3 meters, woody').save()
Leaves(plant=plant, shapes= 'OL', desc= 'Dark green, alternate, serrated, 5-8cm long and 1.5-3.5cm wide', image_name= 'Winterberry_Leaves_Berries.jpg').save()
Berries(plant= plant, colors= 'Red',desc= 'berry, 1cm across', image_name= 'Winterberry_Leaves_Berries.jpg').save()
print(plant.name + ' Complete!!!')

#Wormseed 94
name = 'Wormseed'
Plants(name= name, latin_name= 'Dysphania ambrosioides', isNative= False, image_name= 'Wormseed_Plants.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '1.2 meters, branching').save()
Leaves(plant=plant, shapes= 'OB, LA', desc= '12cm long', image_name= 'Wormseed_Leaves.jpg').save()
Flowers(plant= plant, colors= 'green', desc= 'small, in cluster at top of stem', image_name= 'Wormseed_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Yellow Archangel 95
name = 'Yellow Archangel'
Plants(name= name, latin_name= 'Lamiastrum galeobdolon', isNative= False, image_name= 'Yellow_Archangel_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '0.4-0.8 meters, square').save()
Leaves(plant=plant, shapes= 'OL', desc= 'Paired, opposite, large broad oval, toothed margins, underside often purplish', image_name= 'Yellow_Archangel_Leaves.jpg').save()
Flowers(plant= plant, colors= 'White, Yellow', desc= 'in whorls on terminal spike', image_name= 'Yellow_Archangel_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Yellow Hawkweed 96
name = 'Yellow Hawkweed'
Plants(name= name, latin_name= 'Hieracium caespitosum', isNative= False, image_name= 'Yellow_Hawkweed_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '0.3-0.9 meters, Bristly, mostly leafless').save()
Leaves(plant=plant, shapes= 'OL', desc= 'Long, narrow, hairy, mostly at base with some growing on stems', image_name= 'Yellow_Hawkweed_Leaves.jpg').save()
Flowers(plant= plant, colors= 'Yellow', desc= 'similar to dandelion, at top of stalk', image_name= 'Yellow_Hawkweed_Flower.jpg').save()
print(plant.name + ' Complete!!!')

#Yellow Iris 97
name = 'Yellow Iris'
Plants(name= name, latin_name= 'Iris pseudacorus', isNative= False, image_name= 'Yellow_Iris_Plants.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '1-1.5 meters, round, green').save()
Leaves(plant=plant, shapes= 'LA', desc= 'Erect, 90cm long and 3cm wide').save()
Flowers(plant= plant, colors= 'Yellow', desc= 'typical iris form', image_name= 'Yellow_Iris_Flower.jpg').save()
print(plant.name + ' Complete!!!')

#Yellow Loosestrife 98
name = 'Yellow Loosestrife'
Plants(name= name, latin_name= 'Lysimachia punctata', isNative= False, image_name= 'Yellow_Loosestrife_Plants.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= 'Up to 1 meter, tall').save()
Leaves(plant=plant, shapes= 'OL, LA', desc= 'Whorled or opposite, ovate-lanceolate, fine hairs underneath', image_name= 'Yellow_Loosestrife_Leaves.jpg').save()
Flowers(plant= plant, colors= 'Yellow', desc= 'at top of stem', image_name= 'Yellow_Loosestrife_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Yellow Rocket 99
name = 'Yellow Rocket'
Plants(name= name, latin_name= 'Barbarea vulgaris', isNative= False, image_name= 'Yellow_Rocket_Plant.jpg').save()
plant = Plants.objects.filter(name= name).first()
Stems(plant= plant, desc= '0.3-0.9 meters, Ribbed, hairless').save()
Leaves(plant=plant, shapes= 'OL', desc= 'Deep green, fairly thick', image_name= 'Yellow_Rocket_Leaves.jpg').save()
Flowers(plant= plant, colors= 'Yellow', desc= 'clustered on spikes at end of stems', image_name= 'Yellow_Rocket_Flowers.jpg').save()
print(plant.name + ' Complete!!!')

#Blank, use to add more if desired
#name = ''
#Plants(name= name, latin_name= '', isNative= False , image_name= '').save()
#plant = Plants.objects.filter(name= name).first()
#Stems(plant= plant, desc= '').save()
#Leaves(plant=plant, shapes= '', desc= '').save()
#Flowers(plant= plant, colors= '', desc= '').save()
#Berries(plant= plant, colors= '',desc= '').save()
#print(plant.name + ' Complete!!!')

print("Everything is filled!!!")