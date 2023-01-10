import pandas as pd
from datetime import datetime

from member.models import Contact

def filter_field(field: str):
    if not field:
        return None
    field = str(field).strip()
    if field.lower() == 'nan':
        return None
    return field
    

def fill_data_from_xlsx(filename: str):
    df = pd.read_excel(filename)
    for _, row in df.iterrows():
        try:
            obj, created = Contact.objects.get_or_create(
                name=row['이름'],
                student_id=row['학번'],
                join_year=int(row['기수'][:-1]),
            )
            obj.birth = datetime.strptime(str(row['생년월일']), '%y%m%d') if len(str(row['생년월일'])) == 6 else datetime.strptime(str(row['생년월일']), '%Y. %m. %d') if filter_field(row['생년월일']) else None
            obj.email = row['이메일'] if filter_field(row['이메일']) else None
            
            mobile = str(row['연락처']) if filter_field(row['연락처']) else None
            if len(str(mobile)) == 10:
                mobile = '0'+str(mobile)
                mobile = mobile[:3] + '-' + mobile[3:7] + '-' + mobile[7:]
            obj.mobile = mobile
            
            obj.role = row['직급'] if filter_field(row['직급']) else None
            obj.major = row['소속'] if filter_field(row['소속']) else None
            obj.grade = str(row['학년']) if filter_field(row['학년']) else None
            obj.status = row['회원구분'] if filter_field(row['회원구분']) else None
            obj.study_class = row['스터디 반'] if filter_field(row['스터디 반']) else None
            obj.memo = row['Unnamed: 11'] if filter_field(row['Unnamed: 11']) else None
            obj.save()
        except Exception as e:
            print(e.with_traceback())