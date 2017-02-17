'''
Add the pretty table display
Find deliveries without returns

Think of some other things to add
'''
import Tkinter
import pandas as pd
import matplotlib.pyplot as plt

import formatting


def read_transactions(trans_file): 
    transactions_raw = pd.read_csv(trans_file, delimiter='\t') 
    transactions = transactions_raw.apply(formatting.formatter)
    return transactions


def count_tracking(transactions, cyl_type):
    cyl_type = cyl_type.upper()
    cyl_trans = transactions[transactions['Stock Number'] == cyl_type]

    #Display the data included on the plot
    counts = cyl_trans[['Date', 'Invoice', 'Ending Balance']].to_string(index=False)
    root = Tkinter.Tk()
    root.title('Cylinder Counts')
    info = Tkinter.Label(root, text=counts)
    info.pack()
 
    # Plot the time series
    plt.figure()
    plt.title('{} Transactions'.format(cyl_type))
    plt.ylabel('# of Cylinders Rented')
    plt.plot_date(formatting.date_format(cyl_trans['Date']),
                  cyl_trans['Ending Balance'])
    plt.plot_date(formatting.date_format(cyl_trans['Date']),
                  cyl_trans['Ending Balance'], fmt='b-')
    plt.show()

if __name__ == '__main__':
    # Add the following sections to individual python/batch scripts run from
    # the command line

    # Count Tracking
    count_tracking(read_transactions('/Users/Jesse/Desktop/uniwrecking_all.csv'))

    #Deliveries with no returns
