Name:		akonadi
Summary:	An extensible cross-desktop storage service for PIM
Version:	1.9.0
Release:	1
Epoch:		1
Url:		http://pim.kde.org/akonadi/
License:	LGPLv2+
Group:		Networking/WWW
%define is_beta %(if test `echo %version |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %is_beta
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	ftp://ftp.kde.org/pub/kde/%ftpdir/akonadi/src/%{name}-%{version}.tar.bz2
BuildRequires:	qt4-devel
BuildRequires:	qt4-qtdbus
BuildRequires:	shared-mime-info >= 0.20
BuildRequires:	kde4-macros
BuildRequires:	libxslt-proc
BuildRequires:	libxml2-utils
BuildRequires:	automoc
BuildRequires:	mysql-devel
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(soprano)
Requires:	qt4-database-plugin-mysql
Requires:	mysql-core
Requires:	mysql-common
# Needed for mysqlcheck  which is used in akonadi
Requires:	mysql-client

%description
An extensible cross-desktop storage service for PIM data and meta data
providing concurrent read, write, and query access.

%files
%{_kde_bindir}/*
%{_sysconfdir}/akonadi
%{_datadir}/dbus-1/services/*
%{_datadir}/mime/packages/akonadi-mime.xml
%{_libdir}/qt4/plugins/sqldrivers/libqsqlite3.so

#------------------------------------------------------

# Need a dummy package to override old one
%package common
Group:		Networking/WWW
Summary:	Dummy package to override old

%description common
Dummy package to override old.

%files common
%doc README

#------------------------------------------------------

%define akonadiprotocolinternals_major 1
%define libakonadiprotocolinternals %mklibname akonadiprotocolinternals %{akonadiprotocolinternals_major}

%package -n %{libakonadiprotocolinternals}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libakonadiprotocolinternals}
%{name} library.

%files -n %{libakonadiprotocolinternals}
%{_kde_libdir}/libakonadiprotocolinternals.so.%{akonadiprotocolinternals_major}*

#------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libakonadiprotocolinternals} = %{EVRD}
Requires:	akonadi-common = %{EVRD}

%description devel
This package contains header files needed if you wish to build applications
based on %{name}

%files devel
%{_kde_includedir}/*
%{_kde_libdir}/*.so
%{_kde_libdir}/pkgconfig/akonadi.pc
%{_kde_libdir}/cmake/Akonadi
%{_kde_datadir}/dbus-1/interfaces/*.xml

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 -DMYSQLD_EXECUTABLE=%{_sbindir}/mysqld -DCONFIG_INSTALL_DIR=%{_sysconfdir}
%make

%install
%makeinstall_std -C build
mkdir %buildroot%_libdir/qt4
mv %buildroot%_libdir/plugins %buildroot%_libdir/qt4/

%changelog
* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:1.8.1-1
- New version 1.8.1

* Sat Aug 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:1.8.0-1
- New version 1.8.0
- Convert BuildRequires to pkgconfig style

* Thu Jun 28 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:1.7.90-1
- Update to 1.7.90
- Drop patch (applied in upstream)
- Drop some no longer needed Conflicts and Obsoletes

* Thu May 10 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:1.7.3-1
- update to 1.7.3

* Tue Apr 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:1.7.1-2
- New cleanup in "akonadictl fsck"

* Mon Apr 09 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:1.7.2-1
- update to 1.7.2

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:1.7.1-1
- update to 1.7.1

* Wed Jan 25 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:1.7.0-1
+ Revision: 768181
- New version 1.7.0

* Wed Dec 14 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:1.6.2-1
+ Revision: 740853
- New version 1.6.2

* Thu Jul 07 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:1.5.80-3
+ Revision: 689291
- Rebuild again akonadi to be 2012

* Thu Jul 07 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:1.5.80-2
+ Revision: 689078
- Rebuild for mdv 2012
- Clean the spec file
- New version 1.5.80

* Sat May 07 2011 Funda Wang <fwang@mandriva.org> 1:1.5.3-1
+ Revision: 672219
- update to new version 1.5.3

* Sun Apr 10 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:1.5.2-1
+ Revision: 652176
- New version

* Mon Mar 14 2011 Funda Wang <fwang@mandriva.org> 1:1.5.1-2
+ Revision: 644446
- rebuild for new boost

* Sat Mar 12 2011 Funda Wang <fwang@mandriva.org> 1:1.5.1-1
+ Revision: 643978
- update to new version 1.5.1

* Sun Jan 23 2011 Funda Wang <fwang@mandriva.org> 1:1.5.0-1
+ Revision: 632414
- update to new version 1.5.0

* Sat Jan 08 2011 Funda Wang <fwang@mandriva.org> 1:1.4.95-1mdv2011.0
+ Revision: 630223
- new version 1.4.95

* Wed Jan 05 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:1.4.91-0.gitf2755b9b.1mdv2011.0
+ Revision: 628809
- Update to git snapshot ( akonadi 1.4.91 )
  Remove patch0, should not be necessary with new MySQL

* Mon Dec 20 2010 Funda Wang <fwang@mandriva.org> 1:1.4.90-1mdv2011.0
+ Revision: 623409
- update to new version 1.4.90

* Mon Dec 13 2010 John Balcaen <mikala@mandriva.org> 1:1.4.80-1mdv2011.0
+ Revision: 620681
- Update to 1.4.80

* Sun Nov 21 2010 Funda Wang <fwang@mandriva.org> 1:1.4.54-1.git20101119.1mdv2011.0
+ Revision: 599448
- new snapshot needed by kdepimlibs

* Fri Oct 08 2010 Funda Wang <fwang@mandriva.org> 1:1.4.52-3.svn1183867.1mdv2011.0
+ Revision: 584270
- new snapshot

* Sat Oct 02 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 1:1.4.52-2mdv2011.0
+ Revision: 582569
- patch1: remove exact sqlite version check, upstream SVN 1167021

* Mon Aug 30 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:1.4.52-1mdv2011.0
+ Revision: 574459
- Update to 1.4.52

* Mon Aug 23 2010 Funda Wang <fwang@mandriva.org> 1:1.4.0-2mdv2011.0
+ Revision: 572120
- rebuild for new boost

* Tue Aug 10 2010 Funda Wang <fwang@mandriva.org> 1:1.4.0-1mdv2011.0
+ Revision: 568517
- update to new version 1.4.0

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix mysql requires

* Wed Jul 28 2010 Funda Wang <fwang@mandriva.org> 1:1.3.90-1mdv2011.0
+ Revision: 562174
- 1.3.90 final

* Wed Jul 21 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:1.3.81-0.1132031.1mdv2011.0
+ Revision: 556303
- Update to new snapshot

* Wed Jun 02 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:1.3.1-11mdv2010.1
+ Revision: 546942
- Add requires
  CCBUG: 59580

* Wed May 26 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:1.3.1-10mdv2010.1
+ Revision: 546143
- Rebuild in release mode

* Wed Apr 07 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:1.3.1-9mdv2010.1
+ Revision: 532668
- Do not use mysq_upgrade before the socket exist

* Tue Apr 06 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:1.3.1-8mdv2010.1
+ Revision: 532012
- Fix P100 ( upstream commit 1111609)
- Replace P1 and P2 by my backport in branch ( P100 )
  BUG: 53815
- Fix patch1 and Patch2 ( after upstream review )

* Sun Apr 04 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:1.3.1-7mdv2010.1
+ Revision: 531234
- Fix typo

* Sun Apr 04 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:1.3.1-6mdv2010.1
+ Revision: 531225
- P2: Try to run mysql_upgrade

* Wed Mar 24 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:1.3.1-5mdv2010.1
+ Revision: 527138
- Add trunk akonadi patches

* Mon Mar 22 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:1.3.1-4mdv2010.1
+ Revision: 526315
- Properly backport previous patch
- Fix the add of some missing tables in the mysql db

* Fri Feb 19 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:1.3.1-3mdv2010.1
+ Revision: 508331
- Fix error in plugin load patch

* Thu Feb 18 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:1.3.1-2mdv2010.1
+ Revision: 507807
- Adapt to new mysql

* Wed Feb 10 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:1.3.1-1mdv2010.1
+ Revision: 503666
- New version 1.3.1

* Mon Feb 08 2010 Anssi Hannula <anssi@mandriva.org> 1:1.3.0-3mdv2010.1
+ Revision: 501882
- rebuild for new boost

* Wed Feb 03 2010 Funda Wang <fwang@mandriva.org> 1:1.3.0-2mdv2010.1
+ Revision: 500054
- rebuild for new boost

* Wed Jan 20 2010 Funda Wang <fwang@mandriva.org> 1:1.3.0-1mdv2010.1
+ Revision: 494001
- New verison 1.3.0

* Wed Jan 06 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:1.2.90-0.1070828.1mdv2010.1
+ Revision: 486982
- New snapshot

* Sun Dec 20 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:1.2.80-0.1064406.1mdv2010.1
+ Revision: 480494
- New snapshot

  + Funda Wang <fwang@mandriva.org>
    - update url

* Thu Nov 12 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:1.2.61-0.1044603.2mdv2010.1
+ Revision: 465101
- Rebuild against new qt

* Wed Nov 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:1.2.61-0.1044603.1mdv2010.1
+ Revision: 460424
- update to a svn snapshot (needed for next kdepimlibs4)

* Tue Sep 29 2009 Anssi Hannula <anssi@mandriva.org> 1:1.2.1-5mdv2010.0
+ Revision: 450957
- require mysql-core instead of full mysql suite on 2010.0+

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Remove kdepim4-runtime requires: Not a good idea, add cyclic dependancies

* Thu Sep 03 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:1.2.1-3mdv2010.0
+ Revision: 428711
- Add Requires

* Mon Aug 31 2009 Helio Chissini de Castro <helio@mandriva.com> 1:1.2.1-2mdv2010.0
+ Revision: 423074
- New upstream release

* Fri Aug 21 2009 Funda Wang <fwang@mandriva.org> 1:1.1.95-7mdv2010.0
+ Revision: 418798
- rebuild for new boost

* Tue Aug 04 2009 Helio Chissini de Castro <helio@mandriva.com> 1:1.1.95-6mdv2010.0
+ Revision: 409518
- Force exclude old akonadi-common

* Thu Jun 25 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.1.95-1mdv2010.0
+ Revision: 388896
- Update to version 1.1.95

* Wed Jun 03 2009 Helio Chissini de Castro <helio@mandriva.com> 1.1.90-1mdv2010.0
+ Revision: 382537
- Update for required 1.1.90 in KDE 4.3 beta. From now we will ditch use a branch svn code for official tarballs releases.

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Update release because of a BS pb
    - Fix file list
    - New snapshot

* Fri May 15 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.1.85-0.968058.1mdv2010.0
+ Revision: 376269
- New snapshot

* Thu May 07 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.1.85-0.964925.1mdv2010.0
+ Revision: 372988
- New snapshot

* Mon May 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.1.85-0.963140.1mdv2010.0
+ Revision: 371521
- Fix file list
- New snapshot

* Fri May 01 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.1.80-0.959021.1mdv2010.0
+ Revision: 369502
- Add soprano as buildrequires
- New snapshot ( needed for kde 4.2.70)

* Thu Mar 26 2009 Funda Wang <fwang@mandriva.org> 1.1.1-3mdv2009.1
+ Revision: 361242
- rebuild for new boost

* Wed Feb 25 2009 Helio Chissini de Castro <helio@mandriva.com> 1.1.1-2mdv2009.1
+ Revision: 344977
- Put requires in right place

* Wed Jan 21 2009 Helio Chissini de Castro <helio@mandriva.com> 1.1.1-1mdv2009.1
+ Revision: 332368
- New upstream version released to match KDE 4.2

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 1.1.0-1mdv2009.1
+ Revision: 323907
- New version 1.1.0

* Wed Dec 10 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0.80-2.895463.1mdv2009.1
+ Revision: 312593
- New snapshot
  Remove patch0:  do not add a patch where a simple CMake argument is enough

  + Funda Wang <fwang@mandriva.org>
    - use patch rather than hardcode defination on paths

* Thu Dec 04 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0.80-2mdv2009.1
+ Revision: 309847
- Move conf files in /etc

* Wed Nov 19 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0.80-1mdv2009.1
+ Revision: 304729
- Fix BuildRequires
- Fix Requires ( thanks to Piggz)

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update to official 1.0.80 tarball

* Tue Oct 28 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0.80-0.876753.1mdv2009.1
+ Revision: 297790
- New snapshot
- Fix Requires
- Fix DMYSQLD_EXECUTABLE

* Mon Sep 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0.0-2mdv2009.0
+ Revision: 278374
- mysqld is required at compile time

* Tue Jul 22 2008 Helio Chissini de Castro <helio@mandriva.com> 1.0.0-1mdv2009.0
+ Revision: 240948
- New upstream final akonadi release

  + Funda Wang <fwang@mandriva.org>
    - fix source and url

* Sun Jul 20 2008 Funda Wang <fwang@mandriva.org> 0.82.0-1mdv2009.0
+ Revision: 238876
- fix conditional building

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream version tied to kde 4.1 beta 2 release

* Wed Jun 11 2008 Helio Chissini de Castro <helio@mandriva.com> 0.81.0-2mdv2009.0
+ Revision: 218191
- Proper interface dir

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Jun 03 2008 Helio Chissini de Castro <helio@mandriva.com> 0.81.0-1mdv2009.0
+ Revision: 214729
- Preparing full 0.81 snapshot

* Fri May 23 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.81.0-0.811818.1mdv2009.0
+ Revision: 210703
- New snapshot

* Fri May 16 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.80.0-3.808261.4mdv2009.0
+ Revision: 208092
- New snapshot ( needed by kdepimlibs4 4.0.74 )
- Rediff patch 0

* Thu May 08 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.80.0-3.805338.4mdv2009.0
+ Revision: 204513
- Fix automoc detection on x86_64
- New snapshot (needed by kdepimlibs 4.0.763)

* Wed May 07 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.80.0-2mdv2009.0
+ Revision: 202655
- Add buildrequires
- Fix file list ( Step 1/2 )

* Mon May 05 2008 Helio Chissini de Castro <helio@mandriva.com> 0.80.0-1mdv2009.0
+ Revision: 201353
- Fixed build using provided tarball on the kdesupport
- Changed akonadi package to akonadi-common and made library depends on that
- New upstream package

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Conflict with old kde4-akonadi
    - Add Obsolete on libakonadiprivate4
    - I do not know if user roo exist but use root instead :D
    - Fix Conflicts and obsoletes
    - Add conflicts to ease upgrade
    - Fix Spec file
      Add Shared-mime-info as BuildRequire
    - Fix version
    - Fix version
    - import akonadi


