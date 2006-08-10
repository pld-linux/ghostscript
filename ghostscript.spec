#
# TODO:
#	- fix svga bcond
#
# Conditional build:
%bcond_without	system_jbig2dec	# build with
%bcond_with	svga		# with svgalib display support (vgalib and lvga256 devices)
%bcond_without	gtk		# without gsx 
#
%define   _name ghostscript
Summary:	PostScript & PDF interpreter and renderer
Summary(de):	PostScript & PDF Interpreter und Renderer
Summary(fr):	Interpréteur et visualisateur PostScript & PDF
Summary(ja):	PostScript ¥¤¥ó¥¿¡¼¥×¥ê¥¿¡¦¥ì¥ó¥À¥é¡¼
Summary(pl):	Bezp³atny interpreter i renderer PostScriptu i PDF
Summary(tr):	PostScript & PDF yorumlayýcý ve gösterici
Name:		%{_name}
Version:	8.54
Release:	0.2
License:	GPL
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/ghostscript/%{_name}-%{version}-gpl.tar.bz2
# Source0-md5:	5d0ad0da8297fe459a788200f0eaeeba
# we need to link with libjpeg recompiled with our parameters
Source2:	ftp://ftp.uu.net/graphics/jpeg/jpegsrc.v6b.tar.gz
# Source2-md5:	dbd5f3b47ed13132f04c685d608a7547
Source5:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{_name}-non-english-man-pages.tar.bz2
# Source5-md5:	9b5953aa0cc155f4364f20036b848585
Patch0:		%{name}-missquotes.patch
Patch1:		%{name}-setuid.patch
Patch2:		%{name}-time_h.patch
Patch3:		%{name}-am.patch
# no device for cdj850 in non-espgs ghostscript
# look for patch in old spec for GNU ghostscript
#Patch4:		%{name}-gdevcd8-fixes.patch
#Patch5:		%{name}-glib.patch
Patch6:		%{name}-ijs_pkgconfig_64.patch
URL:		http://www.ghostscript.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-style-dsssl
BuildRequires:	glib2-devel
%{?with_system_jbig2dec:BuildRequires:	jbig2dec-devel}
# for gsx
%{?with_gtk:BuildRequires:	gtk+-devel}
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	jasper-devel
# Required by 'gdevvglb' device.
%{?with_svga:BuildRequires:	svgalib-devel}
# for documentation regeneration
BuildRequires:	tetex
BuildRequires:	tetex-dvips
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXt-devel
Obsoletes:	ghostscript-afpl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cos nGhostscript is a PostScript interpreter. It can render both PostScript
and PDF compliant files to devices which include an X window, many
printer formats (including support for color printers), and popular
graphics file formats.

%description -l de
Ghostscipt ist ein PostScript-Interpretierer. Er kann sowohl
PostScript als auch PDF-konforme Dateien an Geräte ausgeben, zu denen
ein X-Fenster, viele Druckerformate (einschließlich Support für
Farbdrucker) und gängige Grafikdateiformate zählen.

%description -l fr
Ghostscript est un interpréteur PostScript. Il peut rendre des
fichiers PostScript ou PDF sur des périphériques dont une fenêtre X,de
nombreux types d'imprimantes (dont un support pour imprimantes
couleur), et des formats de fichiers graphiques populaires.

%description -l ja
Ghostscript ¤Ï PostScript ¥¤¥ó¥¿¡¼¥×¥ê¥¿¤Ç¤¹¡£¥Ý¥¹¥È¥¹¥¯¥ê¥×¥È¤È PDF
¤ò¥ì¥ó¥À¥ê¥ó¥°¤·¡¢X window ¤äÂ¾¤Î¥×¥ê¥ó¥¿¥Õ¥©¡¼¥Þ¥Ã¥È¤Ç½ÐÎÏ
¤·¤Þ¤¹¡£¤³¤Î¥Ñ¥Ã¥±¡¼¥¸¤ÏÆüËÜ¸ìÂÐ±þ¤·¤Æ¤¤¤Þ¤¹¡£

%description -l pl
Ghostcript jest interpreterem PostScriptu, jêzyka u¿ywanego do opisu
formatu dokumentu. Ghostscript potrafi przetworzyæ dokument w formacie
PostScript i PDF na szereg postaci wyj¶ciowych: drukarki (w³±czaj±c
kolorowe), okno X-Window i popularne formaty graficzne.

%description -l tr
GhostScript, PostScript ve PDF uyumlu dosyalarý, X penceresinde
gösterebilir ve birçok yazýcýnýn (renkli yazýcýlar dahil) basabileceði
biçime getirebilir.

%package gtk
Summary:	Ghostscript with GTK+ console
Summary(pl):	Ghostscript z konsol± GTK+
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Obsoletes:	ghostscript-afpl-gtk

%description gtk
Ghostscript with GTK+ console.

%description gtk -l pl
Ghostscript z konsol± GTK+.

%package devel
Summary:	libgs header files
Summary(pl):	Pliki nag³ówkowe libgs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	ghostscript-afpl-devel

%description devel
Header files for libgs - ghostscript shared library.

%description devel -l pl
Pliki nag³ówkowe libgs - wspó³dzielonej biblioteki ghostscript.

%package ijs-devel
Summary:	IJS development files
Summary(pl):	Pliki dla programistów IJS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	ghostscript-afpl-ijs-devel

%description ijs-devel
IJS development files.

%description ijs-devel -l pl
Pliki do tworzenia programów z u¿yciem biblioteki IJS.

%package ijs-static
Summary:	Static libijs library
Summary(pl):	Statyczna biblioteka IJS
Group:		Development/Libraries
Requires:	%{name}-ijs-devel = %{version}-%{release}
Obsoletes:	ghostscript-afpl-ijs-static

%description ijs-static
Static libijs library.

%description ijs-static -l pl
Statyczna wersja biblioteki IJS.

%prep
%setup -q -a2 -n %{_name}-%{version}-gpl
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1 -b .am
#%patch4 -p1
#%patch5 -p1
%patch6 -p1
ln -sf jp* jpeg

%build
# workarounds
touch ijs/ijs-config.1
%if %{with system_jbig2dec}
if [ -d jbig2dec ]; then
	rm -rf jbig2dec
fi
%endif
# not really needed with new patch :)
# sed -i -e 's#:$(gsdir)/fonts#:$(gsdir)/fonts:%{_datadir}/fonts:%{_datadir}/fonts/Type1#g' src/Makefile.in
#
%{__libtoolize}
cp -f %{_datadir}/automake/config.sub .
%{__aclocal}
%{__autoconf}
CFLAGS="%{rpmcflags} -DA4"
export CFLAGS
%configure \
	--with-fontpath="%{_datadir}/fonts:%{_datadir}/fonts/Type1" \
	--with-ijs \
	--with-jbig2dec \
	--with-jasper \
	--with-x

# NEEDS patch because no such configure options
#        --with-drivers=ALL%{?with_svga:,vgalib,lvga256} \

cd ijs
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-shared
cd ..

%{__make} \
	docdir=%{_defaultdocdir}/%{_name}-%{version}

%{__make} so \
	docdir=%{_defaultdocdir}/%{_name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/ghostscript/lib,%{_libdir},%{_includedir}/ps}


%{__make} install \
	install_prefix=$RPM_BUILD_ROOT \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	docdir=$RPM_BUILD_ROOT%{_defaultdocdir}/%{_name}-%{version} \
	mandir=$RPM_BUILD_ROOT%{_mandir}


%{__make} soinstall \
	install_prefix=$RPM_BUILD_ROOT \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	docdir=$RPM_BUILD_ROOT%{_defaultdocdir}/%{_name}-%{version} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

cd ijs
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
#	prefix=$RPM_BUILD_ROOT%{_prefix} \
#	bindir=$RPM_BUILD_ROOT%{_bindir} \
#	datadir=$RPM_BUILD_ROOT%{_datadir} \
#	libdir=$RPM_BUILD_ROOT%{_libdir} \
#	includedir=$RPM_BUILD_ROOT%{_includedir} \
#	mandir=$RPM_BUILD_ROOT%{_mandir}
cd ..

install lib/{gs_frsd,pdfopt,pdfwrite}.ps $RPM_BUILD_ROOT%{_datadir}/%{_name}/lib

#install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/%{_name}/lib
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{_name}/doc \
	$RPM_BUILD_ROOT%{_bindir}/*.sh \
	$RPM_BUILD_ROOT%{_mandir}/man1/{ps2pdf1{2,3},gsbj,gsdj,gsdj500,gslj,eps2eps}.1

echo ".so gs.1"     > $RPM_BUILD_ROOT%{_mandir}/man1/ghostscript.1
echo ".so ps2pdf.1" > $RPM_BUILD_ROOT%{_mandir}/man1/ps2pdf12.1
echo ".so ps2pdf.1" > $RPM_BUILD_ROOT%{_mandir}/man1/ps2pdf13.1
echo ".so ps2ps.1"  > $RPM_BUILD_ROOT%{_mandir}/man1/eps2eps.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gsbj.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gsdj.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gsdj500.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gslj.1

bzip2 -dc %{SOURCE5} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

#mv -f $RPM_BUILD_ROOT%{_bindir}/{gsc,gs}
ln -sf gs $RPM_BUILD_ROOT%{_bindir}/gsc
ln -sf gs $RPM_BUILD_ROOT%{_bindir}/ghostscript

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc %{_defaultdocdir}/%{_name}-%{version}
%attr(755,root,root) %{_bindir}/[bdeflpsux]*
%attr(755,root,root) %{_bindir}/gs
%attr(755,root,root) %{_bindir}/wftopfa
%attr(755,root,root) %{_bindir}/gs[!x]*
%attr(755,root,root) %{_bindir}/ijs_*_example
%attr(755,root,root) %{_libdir}/libgs.so.*.*
%attr(755,root,root) %{_libdir}/libijs-*.so
%dir %{_datadir}/%{_name}
%dir %{_datadir}/%{_name}/lib
%{_datadir}/%{_name}/lib/*.*
%dir %{_datadir}/%{_name}/%{version}
%dir %{_datadir}/%{_name}/%{version}/lib
# "*.*" will not match "Fontmap". It is OK.
%{_datadir}/%{_name}/%{version}/lib/*.*
%{_datadir}/%{_name}/%{version}/lib/[!F]*map
%{_datadir}/%{_name}/%{version}/lib/FAPI*map
%config %verify(not md5 mtime size) %{_datadir}/%{_name}/%{version}/lib/Fontmap
%config %verify(not md5 mtime size) %{_datadir}/%{_name}/%{version}/lib/FAPIconfig
%{_datadir}/%{_name}/%{version}/Resource
%{_datadir}/%{_name}/%{version}/examples
%{_mandir}/man*/*
%lang(cs) %{_mandir}/cs/man*/*
%lang(de) %{_mandir}/de/man*/*
%lang(es) %{_mandir}/es/man*/*
%lang(fr) %{_mandir}/fr/man*/*
%lang(pl) %{_mandir}/pl/man*/*

%if %{with gtk}
%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gsx
%endif

%files devel
%defattr(644,root,root,755)
%{_includedir}/ps
%attr(755,root,root) %{_libdir}/libgs.so

%files ijs-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ijs-config
%attr(755,root,root) %{_libdir}/libijs.so
%{_includedir}/ijs
%{_libdir}/libijs.la
%{_pkgconfigdir}/*.pc

%files ijs-static
%defattr(644,root,root,755)
%{_libdir}/libijs.a
