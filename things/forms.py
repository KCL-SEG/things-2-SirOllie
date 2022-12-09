"""Forms of the project."""

# Create your forms here.
from django import forms
from things.models import Thing

class ThingForm(forms.ModelForm):

    class Meta:
        model = Thing
        fields = ("name", "description", "quantity")

        name = forms.CharField(label="name",
                            widget=forms.TextInput(attrs={"placeholder": "e.g. John"}))
        description = forms.CharField(label="Description",
                            widget=forms.Textarea())

        quantity = forms.IntegerField(label="quantity",
                            widget=forms.NumberInput(attrs={"placeholder": "e.g. 88"}))


        #if quantity < 0 or quantity > 50:
            #self.add_error("quantity", "Cannot be blank, less than 0, or more than 50")
        #if len(description) > 120:
            #self.add_error("description", "Cannot be longer than 120 characters")


    def save(self, commit=True):
        super().save(commit=False)

        thing = Thing.objects.create(
            name=self.cleaned_data.get("name"),
            description=self.cleaned_data.get("description"),
            quantity=self.cleaned_data.get("quantity"),
        )

        return lesson_request
    #    thing = Thing.objects.create_user(
        #self.cleaned_data.get("name"),
        #description=self.cleaned_data.get("description"),
        #quantity=self.cleaned_data.get("quantity"),
        #)

        #return thing
