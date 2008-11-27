Summary: An X viewer for DVI files
Name: xdvi
Version: 22.85
Release: %mkrel 1
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

BuildRequires: X11-devel

%description
Xdvi allows you to preview the TeX text formatting system's output .dvi
files on an X Window System.

This xdvi does not come from TeTex distribution.

%prep
%setup -q

%build
%configure
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

