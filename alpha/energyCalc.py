#!usr/bin/env python3

def emev(vPulse):

    """
    calculate the equivalent test pulse energy (MeV)

    calculation follows from equations found on page 5 in 'Range of Alpha Particles in Gas'

    @input:  vpulse - voltage of the test pulse as read from oscilloscope (V)

    @output: equivalentE - equivalent energy of the test pulse in MeV
    """

    #C1 = 0.4095 pF according to the case of the preamplifier
    qtest = (0.4095e-12) * vPulse

    #equivalence relation
    equivalentE = 2.26e13 * qtest

    print('Pulse = %f V' %vPulse)
    print('E = %f MeV' %equivalentE)

    #tuple of input, output
    return (vPulse, equivalentE)
