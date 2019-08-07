"""
Project submitted by: Jonathan Collender

References:
1) Udacity Tutorials
2) https://stackoverflow.com/questions/14533709/basic-python-programming-to-convert-month-number-to-month-name-using-dictionary
3) https://github.com/andandandand/bikeshare/blob/master/bikeshare.py
4) https://www.daniweb.com/programming/software-development/threads/400634/repeatedly-asking-for-input
5) https://docs.scipy.org/
6) https://docs.python.org/
7) https://pandas.pydata.org/

"""


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    This is the check that tests if you have added or typed in the correct details
    Asks user to specify a city, month, and day to analyze.
    
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    #Here I am requesting and input from the user for the City argument
    city = input('Please enter a city: Chicago, New York City or Washington: ')
    #This forms part of my input handling, whereby I am maknig sure that the received input is in lower case
    city = city.lower()
    while True:
            if city == 'chicago' or city == 'new york city' or city == 'washington':
                print("Than you for making a valid city selection. City chosen: {}".format(city))
                break
            else:
                print("\n\nPlease try again\n\n")
                city = input('Please enter a city: Chicago, New York City or Washington ')

    # TO DO: get user input for month (all, january, february, ... , june)
    #Here I am requesting and input from the user for the Month argument
    month = input('Please enter a month: January to December ')
    #This forms part of my input handling, whereby I am maknig sure that the received input is in lower case

    month = month.lower()
    while True:
             if month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june' or month == 'july' or month == 'august' or month == 'september' or month == 'october' or month == 'november' or month == 'december':
                print("Than you for making a valid city selection. Month chosen: {}".format(month))
                break
             else:
                print("\n\nPlease try again\n\n")
                month = input('Please enter a month: January to December ')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #Here I am requesting and input from the user for the Day argument
    day = input('Please enter a day of the week: ')
    #This forms part of my input handling, whereby I am maknig sure that the received input is in lower case
    day = day.lower()
    while True:
            if day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday':
                print("Than you for making a valid city selection. Day chosen: {}".format(day))
                break
            else:
                print("\n\nPlease try again\n\n")
                day = input('Please enter a day of the week: ')



    print("\n\nYou have chosen the city: {}, for the month of: {}, on the day of: {}".format(city,month,day))
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    This is an import piece of information on loading the data
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
	# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october','november','december']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):

    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    comm = df.month.mode()[0]


    # TO DO: display the most common day of week
    df['dow'] = df['Start Time'].dt.weekday_name
    comw = df.dow.mode()[0]


    # TO DO: display the most common start
    df['hour'] = df['Start Time'].dt.hour
    comh = df.hour.mode()[0]



    mondic={1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
    moni = int(comm)
    commo = mondic[moni]

    #Printing the values for the months
    print("\nFrom your selection, the following statisics were found: \n\n")
    print("\nThe most common month was: {}.\n\nThe most common day of the week was: {}.\n\nThe most common starting hour was: {}".format(commo, comw, comh))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    startst = df['Start Station'].value_counts().reset_index()['index'][0]


    # TO DO: display most commonly used end station
    endst = df['End Station'].value_counts().reset_index()['index'][0]


    # TO DO: display most frequent combination of start station and end station trip
    """
    I really struggled with this one. I did read up a lot and did get help with this.

    """
    freqcom = df.groupby(['Start Station', 'End Station']).size().nlargest(1)

    #Printing out the station stats
    print("\nThe most commonly used start station was {}. \n\nThe most commonly used end station was {}.\n\nThe most frequent combination of Start and End stations were:\n\n{}".format(startst,endst,freqcom))
    print("\n\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration. Very important to do this" because it helps with the trips""
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    """
    We have the 2 fields, this is Start Time and End Time.
    I will first need to determine what is the difference between these 2 fields
    When we loaded the data, we aligned the data for Start Time. End Time will need to be set too
    """
    df['End Time'] = pd.to_datetime(df['End Time'])

    """
    Now that this has been completed, I'll need to determine the delta between Start Time and End Times
    """

    df['Delta'] = df['End Time'] - df['Start Time']


    """
    Now that this is known, the Numpy Stats functions may be applied
    """

    #sum for total trip time, mean for avg trip time
    # TO DO: display total travel time
    ttt = np.sum(df['Delta'])

    # TO DO: display mean travel time
    meantt = np.mean(df['Delta'])

    print("The total travel time is: {}\n\nThe mean travel time is: {}".format(ttt,meantt))
    print("\n\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')

    start_time = time.time()
    # TO DO: Display counts of user types
    usert = df['User Type'].value_counts()
    # TO DO: Display counts of gender
    try:
        gendert = df['Gender'].value_counts()
    except:
        gendert = "None in sample set"
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        minby = np.min(df['Birth Year'])
    except:
        minby = "None in sample set"
    try:
        maxby = np.max(df['Birth Year'])
    except:
        maxby = "None in sample set"
    try:
        comby = df['Birth Year'].mode()[0]
    except:
        comby = "None in sample set"


    print("\nThe counts per user are:\n\n{}. \n\nThe counts per gender are: \n\n{}.\n\nThe oldest person's birth date was: {}.\n\nThe youngest person's birth date was: {}.\n\nThe most common birth date was: {}\n\n".format(usert,gendert,minby,maxby,comby))

    print("\n\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """ Display raw data """
    print('\nDisplaying raw data...\n\n')
    req = input('Please state if you would like to see the raw data used for this set. Reply Yes to see the data or No to exit:   ')
    step = 0
    while True:
        if req == 'No' or req == 'no':
            break
        if req == 'Yes' or req == 'yes':
            print(df[step: step + 5])
            print("\n\n")
            req = input('If you would like to see 5 more rows, reply Yes to see the data or No to exit:   ')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
