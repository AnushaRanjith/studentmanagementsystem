from rest_framework import serializers
from studapp.models import Student, LibraryHistory, FeesHistory,User

class LibraryHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryHistory
        fields = '__all__'

        def validate(self, data):
            if data['borrow_date'] > data['return_date']:
                raise serializers.ValidationError("Return date must be after borrow date.")
            return data

class FeesHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FeesHistory
        fields = '__all__'
def validate(self, data):
        """
        Ensure the fee amount is positive.
        """
        if data['amount'] <= 0:
            raise serializers.ValidationError("Amount must be a positive value.")
        return data

class StudentSerializer(serializers.ModelSerializer):
    library_history = LibraryHistorySerializer(many=True, read_only=True)
    fees_history = FeesHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']