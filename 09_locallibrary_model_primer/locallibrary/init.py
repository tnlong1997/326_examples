from catalog import models

# Creates a new instance of a Model object.
record = models.MyModelName(my_field_name='Instance #1')

# Saves the instance to the database.
record.save()

# Modifies the instance and saves it back.
record.my_field_name='New Instance Name'
record.save()

# Creates several instances.
for i in range(2, 10):
    rec = models.MyModelName(my_field_name='Instance #{}'.format(i))
    rec.save()

print(record.id)
print(record.my_field_name)

# Retrieves all instances of our model.
print('All Instances: ')
for rec in models.MyModelName.objects.all():
    print('id={}: {}'.format(rec.id, rec.my_field_name))

# Retrieves all instances of our model with a filter.
print('All Instances: ')
for rec in models.MyModelName.objects.filter(my_field_name__contains='9'):
    print('id={}: {}'.format(rec.id, rec.my_field_name))

# Prints the total number of model instances.
records = models.MyModelName.objects.count()
print('The database contains {} instances of our model MyModelName'
      .format(records))
