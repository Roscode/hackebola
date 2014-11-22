#!/usr/bin/perl 

use warnings;
use strict;
use diagnostics;
use feature qw(say);

#####################
#
# 	Copyright © Andres Breton
#	File: columnator.pl
#
#   Extract desired column pairs for comparison/other IO
#
#####################


##########################
# VARIABLES

my $inFile = $ARGV[0];
my $outFile;

my $column1 = 8; #Change to desired column pairs
my $column2 = 18; #Remember to start count at 0

my ($col1, $col2) = columnPairs($column1, $column2);
my @col1 = @$col1;
my @col2 = @$col2;

my $col1Size = @col1; #Number of
my $col2Size = @col2;


##########################
# CHECKS

if(! $inFile) {
    die "You did not provide an input file", $!;
}


##########################
# USER INPUT




##########################
# SUB

sub columnPairs {
    my ($column1, $column2)= @_;
    
    unless (open(INFILE, "<", $inFile)) {
        die "Can not open input file $inFile", $!;
    }
    
    for (<INFILE>) {
        chomp;
        my @line = split /\t/;
        my $tempCol1 = $line[$column1];
        my $tempCol2 = $line[$column2];
        push @col1, $tempCol1;
        push @col2, $tempCol2;
    }
    return \@col1, \@col2;
    close INFILE;
}


