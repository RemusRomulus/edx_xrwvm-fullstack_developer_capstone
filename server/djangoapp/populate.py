from .models import CarMake, CarModel
from random import randint, choice

def _make_fake_car_name(seed_number=0):
    OUT = ''
    car_names = [
        'Serpent',
        'Pulse',
        'Guerilla',
        'Blaze',
        'Eos',
        'Passion',
        'Essence',
        'Sprite',
        'Baron',
        'Empire',
        'Nimbus',
        'Olympian',
        'Crown',
        'Nebula',
        'Oracle',
        'Paladin',
        'Vulture',
        'Tempest',
        'Spotlight',
        'Radiance',
        'Vanish',
        'Bullet',
        'Epitome',
        'Celestial',
        'Jazz',
        'Parallel',
        'Nimbus',
        'Motive',
        'Blizzard',
        'Escape',
    ]
    style = randint(0,3)
    if style == 0:
        OUT = f'{choice(car_names)} {choice(car_names)}'
    elif style == 1:
        OUT = f'{choice(car_names)[:4]}{choice(car_names)[5:]}'
    elif style == 2:
        OUT = f'{choice(car_names)}-{choice(car_names)[:2]}{choice(car_names)[:2]}'
    else:
        OUT = f'{choice(car_names)} Mk. {randint(3, 300)}'

    print(OUT)
    return OUT

def _make_fake_description(seed_number=0, car_name=''):
    OUT = ''
    adjectives = [
        'Reliable',
        'Efficient',
        'Versatile',
        'Stylish',
        'Modern',
        'Compact',
        'Safe',
        'Innovative',
        'Comfortable',
        'Spacious',
        'Economical',
        'Sleek',
        'Powerful',
        'Agile',
        'Eco-friendly',
        'Affordable',
        'High-tech',
        'Durable',
        'Dynamic',
        'Smooth',
        'Elegant',
        'Opulent',
        'Luxurious',
        'Sophisticated',
        'Prestigious',
        'Plush',
        'Refined',
        'Comfortable',
        'Exclusive',
        'High-end',
    ]
    car_parts = [
        'Driveshaft',
        'Differential',
        'Distributor Cap',
        'Drive Belt',
        'Door Handle',
        'Dashboard Panel',
        'Dome Light',
        'Dipstick Tube',
        'Drum Brakes',
        'Defroster Vent',
        'Nuts and Bolts',
        'Navigation System',
        'Neutral Safety Switch',
        'Nitrous Oxide System',
        'Nose Panel',
        'Nutserts',
        'Needle Bearing',
        'Noise Insulation',
        'Neutral Gear',
        'Nut Cover',
        'Valve',
        'Valve cover',
        'Vacuum pump',
        'Voltage regulator',
        'Vehicle speed sensor',
        'Variable valve timing solenoid',
        'Vapor canister',
        'Voltage stabilizer',
        'Vacuum hose',
        'Valve guide',
    ]

    style = choice([0,1,2,0,1,2,0,1,2,0,1,2,0,1,2])
    if style == 0:
        OUT = f'The car is {choice(adjectives)} and {choice(adjectives)}.'
    elif style == 1:
        OUT = f'This car has a {choice(car_parts)} that is {choice(adjectives)} and everyone says the {car_name} is {choice(adjectives)}'
    else:
        OUT = f'Everyone loves the {choice(car_parts)} that {car_name} makes. The {choice(adjectives)} parts are {choice(car_parts)}, {choice(car_parts)}, and {choice(car_parts)}--and the {choice(car_parts)} is {choice(adjectives)}.'

    print(OUT)
    return OUT

def initiate():
    car_make_data = [
        {
            'name': 'NISSAN',
            'description': _make_fake_description(7, 'NISSAN'),
            'mfgr': 'Japan'
        },
        {
            'name': 'Mercedes',
            'description': _make_fake_description(7, 'Mercedes'),
            'mfgr': 'Germany'
        },
        {
            'name': 'Audi',
            'description': _make_fake_description(7, 'Audi'),
            'mfgr': 'Sweden'
        },
        {
            'name': 'Kia',
            'description': _make_fake_description(7, 'Kia'),
            'mfgr': 'Korea'
        },
        {
            'name': 'Toyota',
            'description': _make_fake_description(7, 'Toyota'),
            'mfgr': 'Japan'
        },
        {
            'name': 'Fjord',
            'description': _make_fake_description(7, 'Fjord'),
            'mfgr': 'USA'
        },
        {
            'name': 'Galaxy',
            'description': _make_fake_description(7, 'Galaxy'),
            'mfgr': 'Mars'
        }
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(
                name=data['name'],
                description=data['description'],
                mfgr=data['mfgr']
            )
        )

    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
        {
            "name":"Pathfinder",
            "type":"SUV",
            "year": 2023,
            "car_make":car_make_instances[0],
            'wheel_count': 8
        },
        {
            "name":"Qashqai", "type":"SUV", "year": 2023, "car_make":car_make_instances[0],
            'wheel_count': 4
        },
        {
            "name":"XTRAIL", "type":"SUV", "year": 2023, "car_make":car_make_instances[0],
            'wheel_count': 3
        },
        {"name":"A-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1],
            'wheel_count': 5
        },
        {"name":"C-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1],
            'wheel_count': 2
        },
        {"name":"E-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1],
            'wheel_count': 4
        },
        {"name":"A4", "type":"SUV", "year": 2023, "car_make":car_make_instances[2],
            'wheel_count': 3
        },
        {"name":"A5", "type":"SUV", "year": 2023, "car_make":car_make_instances[2],
            'wheel_count': 4
        },
        {"name":"A6", "type":"SUV", "year": 2023, "car_make":car_make_instances[2],
            'wheel_count': 4
        },
        {"name":"Sorrento", "type":"SUV", "year": 2023, "car_make":car_make_instances[3],
            'wheel_count': 6
        },
        {"name":"Carnival", "type":"SUV", "year": 2023, "car_make":car_make_instances[3],
            'wheel_count': 4
        },
        {"name":"Cerato", "type":"Sedan", "year": 2023, "car_make":car_make_instances[3],
            'wheel_count': 5
        },
        {"name":"Corolla", "type":"Sedan", "year": 2023, "car_make":car_make_instances[4],
            'wheel_count': 4
        },
        {"name":"Camry", "type":"Sedan", "year": 2023, "car_make":car_make_instances[4],
            'wheel_count': 4
        },
        {"name":"Kluger", "type":"SUV", "year": 2023, "car_make":car_make_instances[4],
            'wheel_count': 3
        }
    ]

    
    for car in range(100):
        cname = _make_fake_car_name(car)
        cdesc = _make_fake_description(car, cname)
        cyear = randint(1100, 2024)
        ctype = choice(CarModel.CAR_TYPES)[1]
        cmake = choice(car_make_instances)
        cwheels = choice(
            [2,2,2,2,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,5,5,6,6,7,7,8,8,9]
        )
        car_model_data.append(
            {
                'name': cname,
                'type': ctype,
                'year': cyear,
                'car_make': cmake,
                'wheel_count': cwheels
            }
        )

    for data in car_model_data:
        print('CAR_MAKE', data['car_make'])
        CarModel.objects.create(
            name=data['name'],
            car_make=data['car_make'],
            model_type=data['type'],
            year=data['year'],
            wheel_count=data['wheel_count']
        )

