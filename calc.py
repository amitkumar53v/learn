def input_value( ):
    global value_1, value_2, option
    value_1, option, value_2 = input(
        '\n-------------------\n' + ' Enter value like:\n   a (+-*/) b' + '\n-------------------\n' ).split( )
    operations( )


def using_input_value( ):
    global value_2, option
    option, value_2 = input(
        '\n\n-------------------\n' + ' Enter value like:\n    (+-*/) b ' + '\n-------------------\n' ).split( )
    operations( )


def operations( ):
    global result_1
    if option == '+':
        result_1 = int( value_1 ) + int( value_2 )
    elif option == '-':
        result_1 = int( value_1 ) - int( value_2 )
    elif option == '*':
        result_1 = int( value_1 ) * int( value_2 )
    elif option == '/':
        result_1 = int( value_1 ) / int( value_2 )

    print( '\n*******************\n' + ' Your answer is: ' + str( result_1 ) + '\n*******************' )

    choice = int( input( '\nType: \n0 to exit\n1 to restart\n2 to continue\n' ) )
    if (choice == 1):
        input_value( )
    elif (choice == 2):
        update( )
    elif (choice == 0):
        print( '\n*******************\n' + '      Bye-Bye     ' + '\n*******************' )
    else:
        print( 'Wrong Input' )


def update( ):
    global value_1
    value_1 = result_1
    using_input_value( )


input_value( )
