%define goarch unknown

%if %{_build_arch} == "x86_64"
%define goarch amd64
%endif

%if %{_build_arch} == "aarch64"
%define goarch arm64
%endif

Summary: Idempotent MySQL/PostgreSQL schema management by SQL
Name: sqldef
Version: 2.4.6
Release: 1
URL: https://github.com/sqldef/sqldef
Source0: https://github.com/sqldef/sqldef/releases/download/v%{version}/mssqldef_linux_%{goarch}.tar.gz
Source1: https://github.com/sqldef/sqldef/releases/download/v%{version}/mysqldef_linux_%{goarch}.tar.gz
Source2: https://github.com/sqldef/sqldef/releases/download/v%{version}/psqldef_linux_%{goarch}.tar.gz
Source3: https://github.com/sqldef/sqldef/releases/download/v%{version}/sqlite3def_linux_%{goarch}.tar.gz
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
* Wed Sep 17 2025 ICHINOSE Shogo <shogo82148@gmail.com> - 2.4.6-1
- bump v2.4.6

* Mon Sep 15 2025 ICHINOSE Shogo <shogo82148@gmail.com> - 2.4.3-1
- bump v2.4.3

* Sun Sep 14 2025 ICHINOSE Shogo <shogo82148@gmail.com> - 2.4.2-1
- bump v2.4.2

* Thu Sep 11 2025 ICHINOSE Shogo <shogo82148@gmail.com> - 2.4.1-1
- bump v2.4.1

* Tue Sep 09 2025 ICHINOSE Shogo <shogo82148@gmail.com> - 2.3.0-1
- bump v2.3.0

* Sun Sep 07 2025 ICHINOSE Shogo <shogo82148@gmail.com> - 2.1.0-1
- bump v2.1.0

* Sat Sep 06 2025 ICHINOSE Shogo <shogo82148@gmail.com> - 2.0.11-1
- bump v2.0.11

* Wed Aug 20 2025 ICHINOSE Shogo <shogo82148@gmail.com> - 2.0.10-1
- bump v2.0.10

* Sun Aug 17 2025 ICHINOSE Shogo <shogo82148@gmail.com> - 2.0.9-1
- bump v2.0.9

* Wed Aug 06 2025 ICHINOSE Shogo <shogo82148@gmail.com> - 2.0.8-1
- bump v2.0.8

* Sat Aug 02 2025 ICHINOSE Shogo <shogo82148@gmail.com> - 2.0.7-1
- bump v2.0.7

* Sat Jul 19 2025 ICHINOSE Shogo <shogo82148@gmail.com> - 2.0.5-1
- bump v2.0.5

* Sat Jun 21 2025 ICHINOSE Shogo <shogo82148@gmail.com> - 2.0.4-1
- bump v2.0.4

* Fri Jun 20 2025 ICHINOSE Shogo <shogo82148@gmail.com> - 2.0.3-1
- bump v2.0.3

* Mon May 26 2025 ICHINOSE Shogo <shogo82148@gmail.com> - 2.0.0-1
- bump v2.0.0

* Mon May 19 2025 ICHINOSE Shogo <shogo82148@gmail.com> - 1.0.7-1
- bump v1.0.7

* Mon Apr 28 2025 ICHINOSE Shogo <shogo82148@gmail.com> - 1.0.6-1
- bump v1.0.6

* Mon Mar 17 2025 ICHINOSE Shogo <shogo82148@gmail.com> - 1.0.5-1
- bump v1.0.5

* Sun Mar 16 2025 ICHINOSE Shogo <shogo82148@gmail.com> - 1.0.4-1
- bump v1.0.4

* Fri Mar 14 2025 ICHINOSE Shogo <shogo82148@gmail.com> - 1.0.3-1
- bump v1.0.3

* Sat Mar 08 2025 ICHINOSE Shogo <shogo82148@gmail.com> - 1.0.1-1
- bump v1.0.1

* Tue Mar 04 2025 ICHINOSE Shogo <shogo82148@gmail.com> - 1.0.0-1
- bump v1.0.0

* Fri Feb 21 2025 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.32-1
- bump v0.17.32

* Mon Feb 17 2025 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.31-1
- bump v0.17.31

* Mon Feb 10 2025 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.30-1
- bump v0.17.30

* Wed Jan 29 2025 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.29-1
- bump v0.17.29

* Sat Jan 25 2025 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.28-1
- bump v0.17.28

* Tue Jan 14 2025 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.27-1
- bump v0.17.27

* Sat Jan 04 2025 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.26-1
- bump v0.17.26

* Fri Jan 03 2025 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.25-1
- bump v0.17.25

* Thu Nov 28 2024 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.24-1
- bump v0.17.24

* Mon Nov 04 2024 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.23-1
- bump v0.17.23

* Wed Oct 30 2024 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.22-1
- bump v0.17.22

* Sun Oct 20 2024 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.21-1
- bump v0.17.21

* Wed Oct 16 2024 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.20-1
- bump v0.17.20

* Fri Sep 13 2024 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.19-1
- bump v0.17.19

* Thu Sep 05 2024 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.18-1
- bump v0.17.18

* Tue Aug 06 2024 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.17-1
- bump v0.17.17

* Thu Aug 01 2024 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.16-1
- bump v0.17.16

* Mon Jul 29 2024 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.15-1
- bump v0.17.15

* Thu Jul 18 2024 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.14-1
- bump v0.17.14

* Sat Jul 13 2024 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.13-1
- bump v0.17.13

* Sun May 26 2024 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.11-1
- bump v0.17.11

* Mon May 20 2024 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.10-1
- bump v0.17.10

* Sun May 19 2024 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.9-1
- bump v0.17.9

* Mon May 13 2024 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.8-1
- bump v0.17.8

* Mon Apr 29 2024 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.7-1
- bump v0.17.7

* Mon Apr 22 2024 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.6-1
- bump v0.17.6

* Sat Mar 30 2024 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.5-1
- bump v0.17.5

* Fri Mar 29 2024 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.4-1
- bump v0.17.4

* Thu Mar 28 2024 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.3-1
- bump v0.17.3

* Sun Mar 24 2024 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.2-1
- bump v0.17.2

* Sat Mar 23 2024 ICHINOSE Shogo <shogo82148@gmail.com> - 0.17.1-1
- bump v0.17.1

* Thu Jan 04 2024 ICHINOSE Shogo <shogo82148@gmail.com> - 0.16.15-1
- bump v0.16.15

* Wed Jan 03 2024 ICHINOSE Shogo <shogo82148@gmail.com> - 0.16.14-1
- bump v0.16.14

* Wed Nov 29 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.16.13-1
- bump v0.16.13

* Thu Nov 16 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.16.12-1
- bump v0.16.12

* Wed Nov 15 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.16.11-1
- bump v0.16.11

* Sat Nov 04 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.16.10-1
- bump v0.16.10

* Tue Oct 03 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.16.9-1
- bump v0.16.9

* Sun Oct 01 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.16.8-1
- bump v0.16.8

* Mon Sep 11 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.16.7-1
- bump v0.16.7

* Mon Sep 04 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.16.6-1
- bump v0.16.6

* Sun Sep 03 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.16.5-1
- bump v0.16.5

* Sun Sep 03 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.16.3-1
- bump v0.16.3

* Sun Sep 03 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.16.2-1
- bump v0.16.2

* Mon May 29 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.16.1-1
- bump v0.16.1

* Sat May 27 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.16.0-1
- bump v0.16.0

* Thu May 25 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.15.27-1
- bump v0.15.27

* Thu May 25 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.15.26-1
- bump v0.15.26

* Wed May 17 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.15.25-1
- bump v0.15.25

* Sun May 07 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.15.24-1
- bump v0.15.24

* Thu May 04 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.15.23-1
- bump v0.15.23

* Sun Mar 26 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.15.22-1
- bump v0.15.22

* Wed Mar 22 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.15.21-1
- bump v0.15.21

* Wed Mar 22 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.15.20-1
- bump v0.15.20

* Wed Mar 22 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.15.19-1
- bump v0.15.19

* Wed Mar 15 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.15.18-1
- bump v0.15.18

* Wed Mar 15 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.15.17-1
- bump v0.15.17

* Wed Mar 15 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.15.16-1
- bump v0.15.16

* Wed Mar 15 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.15.15-1
- bump v0.15.15

* Wed Mar 15 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.15.14-1
- bump v0.15.14

* Wed Mar 15 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.15.13-1
- bump v0.15.13

* Wed Mar 15 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.15.12-1
- bump v0.15.12

* Tue Mar 14 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.15.11-1
- bump v0.15.11

* Tue Mar 14 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.15.10-1
- bump v0.15.10

* Tue Mar 14 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.15.9-1
- bump v0.15.9

* Sun Feb 26 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.15.8-1
- bump v0.15.8

* Fri Feb 24 2023 ICHINOSE Shogo <shogo82148@gmail.com> - 0.15.7-1
- bump v0.15.7

* Tue Dec 20 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.15.6-1
- bump v0.15.6

* Sat Dec 17 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.15.5-1
- bump v0.15.5

* Thu Dec 15 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.15.4-1
- bump v0.15.4

* Wed Dec 14 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.15.3-1
- bump v0.15.3

* Tue Dec 13 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.15.2-1
- bump v0.15.2

* Tue Dec 13 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.15.1-1
- bump v0.15.1

* Mon Dec 05 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.15.0-1
- bump v0.15.0

* Mon Nov 28 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.14.5-1
- bump v0.14.5

* Mon Nov 28 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.14.4-1
- bump v0.14.4

* Mon Nov 28 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.14.3-1
- bump v0.14.3

* Sat Nov 26 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.14.2-1
- bump v0.14.2

* Wed Nov 23 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.14.1-1
- bump v0.14.1

* Fri Nov 18 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.14.0-1
- bump v0.14.0

* Fri Nov 18 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.13.23-1
- bump v0.13.23

* Fri Nov 18 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.13.22-1
- bump v0.13.22

* Fri Nov 18 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.13.21-1
- bump v0.13.21

* Tue Nov 15 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.13.20-1
- bump v0.13.20

* Tue Nov 15 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.13.19-1
- bump v0.13.19

* Sun Nov 06 2022 ICHINOSE Shogo <shogo82148@gmail.com> - 0.13.18-1
- bump v0.13.18

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
