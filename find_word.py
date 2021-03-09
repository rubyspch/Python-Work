columns = ['amount_sold', 'value_sold', 'amount_ordered',  'amount_left', 'value_ordered', 'value_left']

def filter_columns(column, filter_word):
    print('Here are the '+filter_word+ ' columns:')
    for words in column:
        if filter_word in words:
            print(words)
        else:
            continue
           
filter_columns(columns,'sold')