#!/usr/bin/env perl

use utf8;
use strict;
use warnings;
use FindBin;
use File::Basename;

our @options = ('--dryrun');

if (($ENV{GITHUB_EVENT_NAME} || '') eq 'release') {
    @options = ();
}

sub execute {
    my @arg = @_;
    my $cmd = join " ", @arg;
    print "executing: $cmd\n";
    my $ret = system(@arg);
    if ($ret != 0) {
        print STDERR "::warning::failed to execute $cmd";
    }
}

sub package_name {
    my $file = shift;
    my $name = basename $file;
    $name =~ s/-[0-9]+\.[0-9]+\.[0-9]+-[0-9]+\..*$//;
    return $name;
}

sub upload {
    my ($prefix) = @_;
    while (my $rpm = <$FindBin::Bin/../x86_64.build/RPMS/x86_64/*.x86_64.rpm>) {
        my $package = package_name($rpm);
        execute("aws", "s3", "cp", @options, $rpm, "s3://shogo82148-rpm-temporary/$prefix/x86_64/$package/");
    }
    while (my $rpm = <$FindBin::Bin/../aarch64.build/RPMS/aarch64/*.aarch64.rpm>) {
        my $package = package_name($rpm);
        execute("aws", "s3", "cp", @options, $rpm, "s3://shogo82148-rpm-temporary/$prefix/aarch64/$package/");
    }
}

upload "amazonlinux/2";
upload "centos/7";
upload "centos/8";
upload "almalinux/8";
upload "almalinux/9";
upload "rockylinux/8";
upload "rockylinux/9";
