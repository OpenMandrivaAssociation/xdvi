Summary: An X viewer for DVI files
Name: xdvi
Version: 22.85
Release: 6
Url: http://math.berkeley.edu/~vojta/xdvi.html
# encodings.c is GPLv2+ and LGPL and MIT
# read-mapfile.c tfmload.c are from dvips
# remaining is MIT
License: GPLv2+
Group: Publishing
Source0: ftp://dante.ctan.org/pub/tex/dviware/xdvi/%{name}-%{version}.tar.gz
Source1: icons-%{name}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-buildroot
Conflicts: tetex-xdvi
Requires: tetex
Requires: ghostscript
BuildRequires: ghostscript

BuildRequires: X11-devel

%description
Xdvi allows you to preview the TeX text formatting system's output .dvi
files on an X Window System.

This xdvi does not come from TeTex distribution.

%prep
%setup -q

%build
%configure \
    --enable-ps-gs=/usr/bin/gs \
    --with-default-texmf-path=/var/lib/texmf/ \
    --with-default-font-path='/var/lib/texmf/%%q'

%make

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
%makeinstall

mkdir -p %{buildroot}%{_iconsdir}

( cd %{buildroot}%{_iconsdir}
  tar xjvf %SOURCE1 )


mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=XDvi
Comment=DVI files viewer
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-Office-Publishing;
MimeType=application/x-dvi;
EOF

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc FAQ README
%{_bindir}/*
%{_mandir}/man?/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/dvi.png
%{_liconsdir}/dvi.png
%{_miconsdir}/dvi.png



%changelog
* Sun Aug 22 2010 Olivier Thauvin <nanardon@mandriva.org> 22.85-5mdv2011.0
+ Revision: 571997
- fix #60740 (applying suggested changes)

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 22.85-4mdv2010.0
+ Revision: 445923
- rebuild

* Sun Apr 19 2009 Olivier Thauvin <nanardon@mandriva.org> 22.85-3mdv2009.1
+ Revision: 368087
- enable gs interpreter for eps (#45276)

* Sat Mar 28 2009 Funda Wang <fwang@mandriva.org> 22.85-2mdv2009.1
+ Revision: 362018
- rebuild

* Thu Nov 27 2008 Frederik Himpe <fhimpe@mandriva.org> 22.85-1mdv2009.1
+ Revision: 307325
- Update to new version 22.85
- SPEC file clean-ups
- Add dvi mime type to desktop file (bug #45991)

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 22.84-8mdv2009.0
+ Revision: 262308
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 22.84-7mdv2009.0
+ Revision: 256757
- rebuild
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 22.84-5mdv2008.1
+ Revision: 136579
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 22.84-5mdv2007.0
+ Revision: 108968
- rebuild

* Mon Aug 14 2006 Olivier Thauvin <nanardon@mandriva.org> 22.84-4mdv2007.0
+ Revision: 55775
- fix menu (my bad)
- fix menu
- Import xdvi

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 22.84-3mdk
- Fix BuildRequires

* Sat Apr 30 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 22.84-2mdk
- Add requires: tetex

* Tue Jan 04 2005 Olivier Thauvin <thauvin@aerov.jussieu.fr> 22.84-1mdk
- First mdk spec

