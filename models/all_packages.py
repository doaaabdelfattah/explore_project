
import base64
from models import storage
from models.package import Package
from models.base_model import Base, BaseModel


class GetData():
    def all():
        # all packages
        packages_all = storage.all(Package)
        packages_all = sorted(packages_all, key=lambda k: k.package_name)
        return (packages_all)
    
    def filtered(filter_item):
        packages = storage.all(Package)
        filtered_packages = [package for package in packages if filter_item.lower(
        ) in package.package_name.lower()]
        return (filtered_packages)
    
    def decode(packages_decode):
        image_list = []
        for package in packages_decode:
            if hasattr(package, 'image') and package.image:
                image_list.append({'image': base64.b64encode(package.image).decode('utf-8'),
                               'description1': package.description1,
                               'package_name': package.package_name,
                               'price': package.price})
                
        return(image_list)

