%define goarch unknown

%if %{_build_arch} == "x86_64"
%define goarch amd64
%endif

%if %{_build_arch} == "aarch64"
%define goarch arm64
%endif

Summary: Idempotent MySQL/PostgreSQL schema management by SQL
Name: sqldef
Version: 0.13.17
Release: 1
URL: https://github.com/k0kubun/sqldef
Source0: https://github.com/itamae-kitchen/mitamae/releases/download/v%{version}/mssqldef_linux_%{goarch}.tar.gz
Source1: https://github.com/itamae-kitchen/mitamae/releases/download/v%{version}/mysqldef_linux_%{goarch}.tar.gz
Source2: https://github.com/itamae-kitchen/mitamae/releases/download/v%{version}/psqldef_linux_%{goarch}.tar.gz
Source3: https://github.com/itamae-kitchen/mitamae/releases/download/v%{version}/sqlite3def_linux_%{goarch}.tar.gz
License: MIT
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The easiest idempotent MySQL/PostgreSQL/SQLite3/SQL Server schema management by SQL.

This is inspired by Ridgepole but using SQL, so there's no need to remember Ruby DSL.

%prep

%build
tar xzvf %{SOURCE0}
tar xzvf %{SOURCE1}
tar xzvf %{SOURCE2}
tar xzvf %{SOURCE3}

%install
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 -p mssqldef %{buildroot}/%{_bindir}/mssqldef
%{__install} -m 755 -p mysqldef %{buildroot}/%{_bindir}/mysqldef
%{__install} -m 755 -p psqldef %{buildroot}/%{_bindir}/psqldef
%{__install} -m 755 -p sqlite3def %{buildroot}/%{_bindir}/sqlite3def

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/mssqldef
%{_bindir}/mysqldef
%{_bindir}/psqldef
%{_bindir}/sqlite3def

%changelog
* Tue Oct 25 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.13.17-1
- bump v0.13.17

* Tue Oct 25 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.13.16-1
- bump v0.13.16

* Wed Oct 19 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.13.15-1
- bump v0.13.15

* Wed Oct 12 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.13.14-1
- bump v0.13.14

* Wed Oct 12 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.13.13-1
- bump v0.13.13

* Wed Oct 05 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.13.12-1
- bump v0.13.12

* Mon Oct 03 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.13.11-1
- bump v0.13.11

* Sat Oct 01 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.13.10-1
- bump v0.13.10

* Fri Aug 26 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.13.9-1
- bump v0.13.9

* Fri Aug 26 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.13.8-1
- bump v0.13.8

* Sun Aug 14 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.13.7-1
- bump v0.13.7

* Sun Aug 14 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.13.6-1
- bump v0.13.6

* Fri Aug 12 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.13.5-1
- bump v0.13.5

* Thu Aug 11 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.13.4-1
- bump v0.13.4

* Wed Aug 10 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.13.3-1
- bump v0.13.3

* Sun Aug 07 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.13.2-1
- bump v0.13.2

* Sun Aug 07 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.13.1-1
- bump v0.13.1

* Sun Aug 07 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.13.0-1
- bump v0.13.0

* Sun Aug 07 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.12.8-1
- bump v0.12.8

* Fri Jul 22 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.12.7-1
- bump v0.12.7

* Wed Jul 20 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.12.6-1
- bump v0.12.6

* Fri Jul 15 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.12.5-1
- bump v0.12.5
- add Rocky Linux 9 distribution

* Fri Jul 15 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.12.4-1
- bump v0.12.4

* Wed Jul 13 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.12.3-1
- bump v0.12.3

* Tue Jul 12 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.12.2-1
- bump v0.12.2

* Sun Jul 10 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.12.1-1
- bump v0.12.1

* Sat Jul 09 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.12.0-1
- bump v0.12.0

* Sun Jul 03 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.11.62-1
- bump v0.11.62

* Wed Jun 29 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.11.61-1
- bump v0.11.61

* Wed Jun 15 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.11.60-1
- bump v0.11.60

* Tue Jun 14 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.11.59-3
- Do not use SHA1 digests in AlmaLinux9

* Tue Jun 07 2022 ICHINOSE Shogo <shogo82148@gmail.com>
- add AlmaLinux 9 distribution

* Sat May 21 2022 ICHINOSE Shogo <shogo82148@gmail.com>
- bump v0.11.59

* Tue May 17 2022 ICHINOSE Shogo <shogo82148@gmail.com>
- bump v0.11.58

* Wed May 11 2022 ICHINOSE Shogo <shogo82148@gmail.com>
- bump v0.11.57

* Wed May 11 2022 ICHINOSE Shogo <shogo82148@gmail.com>
- bump v0.11.56

* Wed May 11 2022 ICHINOSE Shogo <shogo82148@gmail.com>
- bump v0.11.55

* Wed May 11 2022 ICHINOSE Shogo <shogo82148@gmail.com>
- bump v0.11.54

* Sun May 08 2022 ICHINOSE Shogo <shogo82148@gmail.com>
- bump v0.11.53

* Thu May 05 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.52

* Thu May 05 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.51

* Tue Apr 12 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.50

* Mon Apr 04 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.49

* Fri Apr 01 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.48

* Thu Mar 31 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.47

* Thu Mar 31 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.46

* Tue Mar 15 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.45

* Sat Mar 12 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.44

* Sat Mar 12 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.43

* Sat Mar 12 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.42

* Sat Mar 12 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.41

* Sun Mar 06 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.40

* Sun Mar 06 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.39

* Sun Feb 20 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.38

* Sun Feb 20 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.37

* Wed Feb 16 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.36

* Wed Feb 02 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.35

* Mon Jan 31 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.34

* Mon Jan 31 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.33

* Sun Jan 30 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.32

* Sun Jan 30 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.31

* Wed Jan 26 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.30

* Tue Jan 25 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.29

* Mon Jan 24 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.28

* Mon Jan 24 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.27

* Sun Jan 23 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.26

* Sun Jan 23 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.25

* Sat Jan 22 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.24

* Sat Jan 22 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.23

* Fri Jan 21 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.22

* Fri Jan 21 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.21

* Wed Jan 5 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.20

* Tue Jan 4 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.19

* Tue Jan 4 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.18

* Tue Jan 4 2022 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.17

* Fri Dec 31 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.16

* Sun Dec 12 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.15

* Mon Nov 15 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.14

* Sat Nov 6 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.13

* Sat Nov 6 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.12

* Sun Oct 31 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.11

* Sat Oct 16 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.10

* Sat Oct 16 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.9

* Sat Oct 16 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.8

* Wed Sep 29 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.7

* Tue Sep 28 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.6

* Tue Sep 28 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.5

* Thu Sep 23 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.4

* Sun Sep 19 2021 Ichnose Shogo <shogo82148@gmail.com>
- bump v0.11.3

* Sun Sep 19 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.2

* Sat Sep 18 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.1

* Sat Sep 18 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.0

* Sun Jul 18 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.10.16
