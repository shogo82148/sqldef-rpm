#!/usr/bin/env perl

use v5.38;
use utf8;
use strict;
use FindBin;
use POSIX qw(strftime locale_h);
use Actions::Core;

sub slurp($file) {
    open my $fh, "<", $file or die "failed to open $file: $!";
    local $/ = undef;
    my $content = <$fh>;
    close $fh;
    return $content;
}

sub spew($file, $content) {
    open my $fh, ">", "$file.tmp$$" or die "failed to open $file: $!";
    print $fh $content;
    close $fh or die "failed to close $file: $!";
    rename "$file.tmp$$", $file or die "failed to rename $file.tmp$$ to $file: $!";
}

my $build_sh = slurp("$FindBin::Bin/build.sh");
$build_sh =~ /VERSION=(\d+\.\d+\.\d+)/ or die "failed to parse VERSION from build.sh";
my $current_version = $1;
say STDERR "current version: $current_version";

my $latest_version = `gh release view --repo k0kubun/sqldef --template '{{ .name }}' --json name`;
$latest_version =~ s/^v//;
say STDERR "latest version: $latest_version";
set_output('latest-version', $latest_version);

if ($current_version eq $latest_version) {
    say STDERR "already up-to-date";
    exit 0;
}

say STDERR "updating to $latest_version...";

# update build.sh
$build_sh =~ s/VERSION=\d+\.\d+\.\d+/VERSION=$latest_version/;
spew("$FindBin::Bin/build.sh", $build_sh);

# update sqldef.spec
my $spec = slurp("$FindBin::Bin/../rpmbuild/SPECS/sqldef.spec");
$spec =~ s/Version:\s+\d+\.\d+\.\d+/Version: $latest_version/;
$spec =~ s/Release:\s+\d+/Release 1/;
setlocale(LC_TIME, "C");
my $date = strftime "%a %b %d %Y", localtime;
my $changelog = <<"END";
%changelog
* $date ICHINOSE Shogo <shogo82148\@gmail.com> - ${latest_version}-1
- bump v${latest_version}
END
$spec =~ s/%changelog/$changelog/;
spew("$FindBin::Bin/../rpmbuild/SPECS/sqldef.spec", $spec);
