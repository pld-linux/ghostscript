Summary:	PostScript interpreter and renderer
Summary(de):	PostScript-Interpreter und Renderer
Summary(fr):	Interpréteur et visualisateur PostScript
Summary(pl):	Bezp³atny interpreter PostScriptu
Summary(tr):	PostScript yorumlayýcý ve gösterici
Name:		ghostscript
Version:	5.10
Release:	3
Group:		Applications/Graphics
Group(pl):	Aplikacje/Grafika
Copyright:	GPL
URL:		http://www.cs.wisc.edu/~ghost/
Source0:	ftp://ftp.cs.wisc.edu/ghost/gnu/gs510/%{name}-%{version}.tar.gz
Source1:	pdf_sec.ps
Icon:		ghost.gif
Patch0:		%{name}-%{version}-config.patch
Patch1:		%{name}-%{version}-post.patch
Patch2:		%{name}-%{version}-devices.patch
Patch3:		%{name}-%{version}-shared_libs.patch
Vendor:		Aladdin Enterprises
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Ghostscript is a PostScript interpretor. It can render both PostScript
and PDF compliant files to devices which include an X window, many printer
formats (including support for color printers), and popular graphics
file formats.

%description -l de
Ghostscipt ist ein PostScript-Interpretierer. Er kann sowohl PostScript als
auch PDF-konforme Dateien an Geräte ausgeben, zu denen ein X-Fenster, 
viele Druckerformate (einschließlich Support für Farbdrucker) und gängige
Grafikdateiformate zählen.

%description -l fr
Ghostscript est un interpréteur PostScript. Il peut rendre des fichiers
PostScript ou PDF sur des périphériques dont une fenêtre X,de nombreux
types d'imprimantes (dont un support pour imprimantes couleur), et des
formats de fichiers graphiques populaires.

%description -l pl
Ghostcript jest interpreterem PostScriptu, jêzyku u¿ywanego do opisu formatu
dokumentu. Ghostscript potrafi przetworzyæ dokument w formacie PostScript
i PDF %{name} szereg postaci wyj¶ciowych: drukarki (w³±czaj±c kolorowe), okno
X-Window i popularne formaty graficzne.

%description -l tr
GhostScript, PostScript ve PDF uyumlu dosyalarý, X penceresinde gösterebilir
ve birçok yazýcýnýn (renkli yazýcýlar dahil) basabileceði biçime getirebilir.

%prep
%setup -q -n gs%{version}
ln -s unix-gcc.mak Makefile
%patch0 -p1 
%patch1 -p1 
%patch2 -p1
%patch3 -p1

%build
install %SOURCE1 .
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS -w" prefix=/usr

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,man,doc}

make install prefix=$RPM_BUILD_ROOT/usr

echo .so gs.1 > $RPM_BUILD_ROOT%{_mandir}/man1/ghostscript.1

ln -sf gs 	$RPM_BUILD_ROOT/usr/bin/ghostscript

strip 		$RPM_BUILD_ROOT/usr/bin/gs

gzip -9nf 	$RPM_BUILD_ROOT%{_mandir}/man1/*

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(644,root,root) %docdir /usr/doc/%{name}-%{version}

%attr(755,root,root) /usr/bin/*

%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{version}/*.ps
%config %verify(not size md5 mtime) %{_datadir}/%{name}/%{version}/Fontmap

%dir %{_datadir}/%{name}/%{version}/examples
%{_datadir}/%{name}/%{version}/examples/*.ps

%{_mandir}/man1/*

%changelog
* Tue Feb 16 1999 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- added support for encrypted PDFs

* Sat Feb 13 1999 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
[5.10-2d]
- added devices patch (more drivers - i.e. for Epson Stylus Color)
- added shared_libs patch (now gs is dynamicly linked with
  existing libjpeg, libpng and libz)
- gzipping man pages instead bzip2ing
- removed copying makefile from %setup section (ln -s instead)

* Sun Jan 10 1999 Ziemek Borowski <ziembor@faq-bot.ziembor.waw.pl> 
[5.10] 
- based on Russell Lang   http://www.cs.wisc.edu/~ghost/rjl.html spec 
updated to 5.10 

* Sun Nov 15 1998 Marcin Korzonek <mkorz@shadow.eu.org>
- build agains glibc 2.1,
- fixed files permission according to PLD-devel policy,
- translations modified for pl,
- spec rewritten with usage of %%name and %%version macros,
  for easy upgrade.
- location of source files changed to regular URL expression 

* Thu Jul  2 1998 Jeff Johnson <jbj@redhat.com>
- updated to 4.03.

* Tue May 05 1998 Cristian Gafton <gafton@redhat.com>
- enabled more printer drivers
- buildroot

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Mar 03 1997 Erik Troan <ewt@redhat.com>
- Made %{_datadir}/ghostscript/3.33/Fontmap a config file.
