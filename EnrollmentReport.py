import pandas as pd

import os
for dirname, _, filenames in os.walk('/PycharmProjects/EnrollmentReport'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

enrollment = pd.read_csv('../EnrollmentReport/' + input("Enter CSV file:"))
enrollment = enrollment.rename(columns={'Current Eligibility End': 'End', 'plan': 'Plan', 'Plan Status': 'Status', 'Previous Plan':'Previous'})
enrollment['Region'] = enrollment['Region'].fillna('Metro')
enrollment['End'] = pd.to_datetime(enrollment['End'])
enrollment.head()

print("---------Current------")
current = enrollment.loc[(enrollment.Status == 'Enrolled')]
current = current[(current['Plan'] != 'CONORX  ') & (current['Plan'] != 'COPA    ')]
print(current.groupby(['Region', 'Plan']).Plan.count())

#First Month Params
start_date = input("enter one-month start date yyyy-mm-dd format:")
end_date = input("enter one-month end date yyyy-mm-dd format:")
mask = (enrollment['End'] > start_date) & (enrollment['End'] <= end_date)
month_one = enrollment.loc[mask]

#Second Month Params
start_date = input("enter two-month start date yyyy-mm-dd format:")
end_date = input("enter two-month end date yyyy-mm-dd format:")
mask = (enrollment['End'] > start_date) & (enrollment['End'] <= end_date)
month_two = enrollment.loc[mask]

#Third Month Params
start_date = input("enter three-month start date yyyy-mm-dd format:")
end_date = input("enter three-month end date yyyy-mm-dd format:")
mask = (enrollment['End'] > start_date) & (enrollment['End'] <= end_date)
month_three = enrollment.loc[mask]

print("----------One Month Expired---------")
month_one = month_one[(month_one['Previous'] != 'CONORX  ') & (month_one['Previous'] != 'COPA    ')]
print(month_one.groupby(['Region', 'Previous']).Previous.count())

print("----------Two Month Expired---------")
month_two = month_two[(month_two['Previous'] != 'CONORX  ') & (month_two['Previous'] != 'COPA    ')]
print(month_two.groupby(['Region', 'Previous']).Previous.count())

print("----------Three Month Expired---------")
month_three = month_three[(month_three['Previous'] != 'CONORX  ') & (month_three['Previous'] != 'COPA    ')]
print(month_three.groupby(['Region', 'Previous']).Previous.count())