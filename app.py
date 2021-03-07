#!/usr/bin/env python
import click


@click.command()
@click.option('--type')
@click.option('--temp',type=float)
def conversion(type,temp):
    
    '''
    A conversion of celsius to fahrenheit.
    formula (0°C × 9/5) + 32 = 32°F
    '''
    
    if type == 'F':
        result = (temp-32)/(9/5)
    elif type == 'C':
        result = (temp*9/5)+32
    else:
        result = 'Please specify the type of temperature'
    
    click.echo(result)
if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    conversion()
